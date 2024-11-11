"""Downloads data from FAOSTAT website."""

import time
from datetime import datetime

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
