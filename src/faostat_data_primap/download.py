"""Downloads data from FAOSTAT website."""

import time
import zipfile
from datetime import datetime

import requests
from bs4 import BeautifulSoup

# from helper.definitions import downloaded_data_path, root_path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from src.faostat_data_primap.exceptions import DateTagNotFoundError


def get_html_content(url):
    """
    Get html from url.

    Parameters
    ----------
    url

    Returns
    -------
        html content
    -------

    """
    # If the driver isn't found on your system PATH, Selenium
    # will automatically download it for you. Make sure there is no
    # chromedriver installed on your system
    service = Service()
    driver = webdriver.Chrome(service=service)

    driver.get(url)

    # give time to load javascript
    time.sleep(3)

    html_content = driver.page_source

    return BeautifulSoup(html_content, "html.parser")


def get_last_updated_date(soup, url):
    """
    Get the date when data set way last updated from html text

    Parameters
    ----------
    soup
    url

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


def download_file(url_download, save_path):
    """
    todo

    Parameters
    ----------
    url_download
    save_path

    Returns
    -------
        True if the file was downloaded, False if a cached file was found
    """
    if not save_path.exists():
        response = requests.get(url_download, timeout=20)
        response.raise_for_status()

        # will overwrite existing file
        with open(save_path, mode="wb") as file:
            file.write(response.content)
        return True
    else:
        print(f"Skipping {save_path}" " because it already exists.")
    return False


def unzip_file(local_filename):
    """
    todo

    Parameters
    ----------
    local_filename

    Returns
    -------
        List of unzipped files
    """
    # unzip data (only for new downloads)
    if local_filename.suffix == ".zip":
        try:
            # TODO check if unzipped files already there
            zipped_file = zipfile.ZipFile(str(local_filename), "r")
            zipped_file.extractall(str(local_filename.parent))
            print(f"Extracted {len(zipped_file.namelist())} files.")
            zipped_file.close()
        # TODO Better error logging/visibilty
        except zipfile.BadZipFile:
            print(f"Error while trying to extract " f"{local_filename}")
        except NotImplementedError:
            print("Zip format not supported, " "please unzip on the command line.")
    else:
        print(f"Not attempting to extract " f"{local_filename}.")
