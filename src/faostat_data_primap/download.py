"""Downloads data from FAOSTAT website."""

import hashlib
import os
import pathlib
import time
import zipfile
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

from faostat_data_primap.exceptions import DateTagNotFoundError
from faostat_data_primap.helper.definitions import domains, downloaded_data_path


def find_previous_release_path(
    current_release_path: pathlib.Path,
) -> pathlib.Path | None:
    """
    Find the most recent previous release directory within same domain

    Release directories are assumed to be subdirectories within the same parent
    directory as `current_release_path`. The Sorting is done alphabetically,
    so directory names should follow the naming convention YYYY-MM-DD

    Parameters
    ----------
    current_release_path : pathlib.Path
        The path of the current release directory.

    Returns
    -------
    pathlib.Path or None
        Returns the path of the most recent previous release directory if one exists,
        otherwise returns None.
    """
    domain_path = current_release_path.parent
    all_releases = [
        release_name
        for release_name in os.listdir(current_release_path.parent)
        if (domain_path / release_name).is_dir()
    ]

    # make sure all directories follow the naming convention
    try:
        all_releases_datetime = [
            datetime.strptime(release, "%Y-%m-%d") for release in all_releases
        ]
    except ValueError as e:
        msg = (
            "All release folders must be in YYYY-MM-DD format, "
            f"got {sorted(all_releases)}"
        )
        raise ValueError(msg) from e

    all_releases_datetime = sorted(all_releases_datetime)
    current_release_datetime = datetime.strptime(current_release_path.name, "%Y-%m-%d")
    index = all_releases_datetime.index(current_release_datetime)

    # if the current release is the latest or the only one
    if index == 0:
        return None

    return domain_path / all_releases_datetime[index - 1].strftime("%Y-%m-%d")


def calculate_checksum(file_path: pathlib.Path) -> str:
    """
    Calculate the SHA-256 checksum of a file.

    Parameters
    ----------
    file_path : pathlib.Path
        The path to the file for which the checksum is calculated.

    Returns
    -------
    str
        The SHA-256 checksum of the file as a hexadecimal string.
    """
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def download_methodology(url_download: str, save_path: pathlib.Path) -> None:
    """
    Download methodology file.

    Download the methodology PDF-file from a specified URL and save to a
    target directory. If the file already exists in `save_path`,
    the download is skipped. If a previous release directory exists,
    the function attempts to locate the file there and compares checksums
    to avoid downloading an identical file. If it exists in the previous release,
    but it's not identical it is downloaded. If the file exists in the previous
    release directory and is identical, a symlink will be created instead of downloading
    to avoid duplicate downloads. If the file does not exist in a previous release,
    it will be downloaded.

    Parameters
    ----------
    url_download : str
        The URL from which to download the file.
    save_path : pathlib.Path
        The path to the directory where the file should be saved.
    """
    filename = url_download.split("/")[-1]
    download_path = save_path / filename

    if not save_path.exists():
        save_path.mkdir()

    if download_path.exists():
        print(f"Skipping download of {download_path} because it already exists.")
        return

    previous_release = find_previous_release_path(save_path)
    # Attempt to find a file to compare in the previous release
    if previous_release:
        file_to_compare = previous_release / filename
        if file_to_compare.exists():
            response = requests.get(url_download, stream=True, timeout=30)
            response.raise_for_status()
            file_to_download_checksum = hashlib.sha256(response.content).hexdigest()
            file_to_compare_checksum = calculate_checksum(file_to_compare)

            if file_to_download_checksum == file_to_compare_checksum:
                print(
                    f"File '{filename}' is identical in the previous release. "
                    f"Creating symlink."
                )
                os.symlink(file_to_compare, download_path)
                return
            else:
                print(
                    f"File '{filename}' differs from previous release. "
                    f"Downloading file."
                )
        else:
            print(f"File '{filename}' not found in previous release. Downloading file.")
            response = requests.get(url_download, stream=True, timeout=30)
            response.raise_for_status()

        # Save downloaded file to current release
        with open(download_path, "wb") as f:
            f.write(response.content)

    else:
        print(f"No previous release found. Downloading file '{filename}'.")
        response = requests.get(url_download, stream=True, timeout=30)
        response.raise_for_status()
        print(download_path)
        with open(download_path, "wb") as f:
            f.write(response.content)


def get_html_content(url: str) -> BeautifulSoup:
    """
    Get html from url.

    Parameters
    ----------
    url
        The url to the domain overview website.

    Returns
    -------
        html content
    """
    # If the chrome driver isn't found on your system PATH, Selenium
    # will automatically download it for you. Make sure there is no
    # chromedriver installed on your system.
    service = Service()
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(url)

    # give time to load javascript
    time.sleep(3)

    html_content = driver.page_source

    return BeautifulSoup(html_content, "html.parser")


def get_last_updated_date(soup: BeautifulSoup, url: str) -> str:
    """
    Get the date when data set way last updated from html text

    The FAO stat domain overview page includes a date when
    the data set was last updated. We need it to label our downloaded
    data sets. This function searches and extracts the date
    from the html code.

    Parameters
    ----------
    soup
        The beautiful soup object with all html code of the domain
        overview page.
    url
        The url to the domain overview page.

    Returns
    -------
        date when data set was last updated

    Raises
    ------
    DateTagNotFoundError
        If the tag for the date is not found in the html code
    """
    date_tag = soup.find("p", {"data-role": "date"})

    if not date_tag:
        raise DateTagNotFoundError(url=url)

    last_updated = date_tag.get_text()
    last_updated = datetime.strptime(last_updated, "%B %d, %Y").strftime("%Y-%m-%d")
    return last_updated


def download_file(url_download: str, save_path: pathlib.Path) -> bool:
    """
    Download file.

    If an existing file is found at this location, the download is skipped.

    Parameters
    ----------
    url_download
        Remote URL to download the file from
    save_path
        Path to save the downloaded file to

    Returns
    -------
        True if the file was downloaded, False if a cached file was found
    """
    if not save_path.exists():
        with requests.get(url_download, stream=True, timeout=30) as response:
            response.raise_for_status()

            with open(save_path, mode="wb") as file:
                file.write(response.content)

        return True
    else:
        print(f"Skipping download of {save_path}" " because it already exists.")
    return False


def unzip_file(local_filename: pathlib.Path) -> list[str]:
    """
    Unzip files in same directory. Skip if files are already there

    Parameters
    ----------
    local_filename
        Path to the zip file

    Returns
    -------
        List of unzipped files
    """
    unzipped_files = []
    if local_filename.suffix == ".zip":
        try:
            with zipfile.ZipFile(str(local_filename), "r") as zip_file:
                for file_info in zip_file.infolist():
                    extracted_file_path = local_filename.parent / file_info.filename

                    if extracted_file_path.exists():
                        print(
                            f"File '{file_info.filename}' already exists. "
                            f"Skipping extraction."
                        )
                    else:
                        print(f"Extracting '{file_info.filename}'...")
                        zip_file.extract(file_info, local_filename.parent)
                        unzipped_files.append(local_filename.name)

        # TODO Better error logging/visibilty
        except zipfile.BadZipFile:
            print(f"Error while trying to extract " f"{local_filename}")
        except NotImplementedError:
            print("Zip format not supported, " "please unzip on the command line.")
    else:
        print(f"Not attempting to extract " f"{local_filename}.")
    return unzipped_files


def download_all_domains(
    domains: dict[str, dict[str, str]] = domains,
    downloaded_data_path: pathlib.Path = downloaded_data_path,
) -> list[str]:
    """
    Download and unpack all climate-related domains from the FAO stat website.

    Extract the date when the data set was last updated and create a directory
    with the same name. Download the zip files for each domain if
    it does not already exist. Unpack the zip file and save in
    the same directory.

    Parameters
    ----------
    sources
        Name of data set, url to domain overview,
        and download url

    Returns
    -------
        List of input files that have been fetched or found locally.

    """
    downloaded_files = []
    for ds_name, urls in domains.items():
        url = urls["url_domain"]
        url_download = urls["url_download"]
        url_methodology = urls["url_methodology"]

        soup = get_html_content(url)

        last_updated = get_last_updated_date(soup, url)

        if not downloaded_data_path.exists():
            downloaded_data_path.mkdir()

        ds_path = downloaded_data_path / ds_name
        if not ds_path.exists():
            ds_path.mkdir()

        local_data_dir = ds_path / last_updated
        if not local_data_dir.exists():
            local_data_dir.mkdir()

        download_methodology(save_path=local_data_dir, url_download=url_methodology)

        local_filename = local_data_dir / f"{ds_name}.zip"

        download_file(url_download=url_download, save_path=local_filename)

        downloaded_files.append(str(local_filename))

        unzip_file(local_filename)

    return downloaded_files
