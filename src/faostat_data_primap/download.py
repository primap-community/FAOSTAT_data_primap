"""Downloads data from FAOSTAT website."""

import pathlib
import time
import zipfile
from datetime import datetime

import bs4
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from src.faostat_data_primap.exceptions import DateTagNotFoundError


def get_html_content(url: str) -> bs4.BeautifulSoup:
    """
    Get html from url.

    Parameters
    ----------
    url
        The url to the domain overview website.

    Returns
    -------
        html content
    -------

    """
    # If the chrome driver isn't found on your system PATH, Selenium
    # will automatically download it for you. Make sure there is no
    # chromedriver installed on your system.
    service = Service()
    driver = webdriver.Chrome(service=service)

    driver.get(url)

    # give time to load javascript
    time.sleep(3)

    html_content = driver.page_source

    return BeautifulSoup(html_content, "html.parser")


def get_last_updated_date(soup: bs4.BeautifulSoup, url: str) -> str:
    """
    Get the date when data set way last updated from html text

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
    """
    date_tag = soup.find("p", {"data-role": "date"})

    if not date_tag:
        raise DateTagNotFoundError(url=url)

    last_updated = date_tag.get_text()
    last_updated = datetime.strptime(last_updated, "%B %d, %Y").strftime("%Y-%m-%d")
    return last_updated


def download_file(url_download: str, save_path: pathlib.PosixPath):
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


def unzip_file(local_filename: pathlib.PosixPath):
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
                        unzipped_files.append(local_filename)

        # TODO Better error logging/visibilty
        except zipfile.BadZipFile:
            print(f"Error while trying to extract " f"{local_filename}")
        except NotImplementedError:
            print("Zip format not supported, " "please unzip on the command line.")
    else:
        print(f"Not attempting to extract " f"{local_filename}.")
    return unzipped_files
