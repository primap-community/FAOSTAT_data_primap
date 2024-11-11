"""Downloads data from FAOSTAT website."""

import time
import zipfile
from datetime import datetime

import datalad.api
from bs4 import BeautifulSoup
from helper.definitions import downloaded_data_path, root_path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class DateTagNotFoundError(Exception):
    """
    The date when the data set was last updated could not be found
    """


def __init__(
    self, message="The <p> tag with data-role='date' was not found on the page."
):
    super().__init__(message)


if __name__ == "__main__":
    sources = [
        (
            "farm_gate_emissions_crops",
            "https://www.fao.org/faostat/en/#data/GCE",
            "https://bulks-faostat.fao.org/production/Emissions_crops_E_All_Data.zip",
        ),
        (
            "farm_gate_livestock",
            "https://www.fao.org/faostat/en/#data/GLE",
            "https://bulks-faostat.fao.org/production/Emissions_livestock_E_All_Data.zip",
        ),
        (
            "farm_gate_agriculture_energy",
            "https://www.fao.org/faostat/en/#data/GN",
            "https://bulks-faostat.fao.org/production/Emissions_Agriculture_Energy_E_All_Data.zip",
        ),
        (
            "land_use_forests",
            "https://www.fao.org/faostat/en/#data/GF",
            "https://bulks-faostat.fao.org/production/Emissions_Land_Use_Forests_E_All_Data.zip",
        ),
        (
            "land_use_fires",
            "https://www.fao.org/faostat/en/#data/GI",
            "https://bulks-faostat.fao.org/production/Emissions_Land_Use_Fires_E_All_Data.zip",
        ),
        (
            "land_use_drained_organic_soils",
            "https://www.fao.org/faostat/en/#data/GV",
            "https://bulks-faostat.fao.org/production/Emissions_Drained_Organic_Soils_E_All_Data.zip",
        ),
        (
            "pre_post_agricultural_production",
            "https://www.fao.org/faostat/en/#data/GPP",
            "https://bulks-faostat.fao.org/production/Emissions_Pre_Post_Production_E_All_Data.zip",
        ),
    ]
    for (
        ds_name,
        url,
        url_download,
    ) in sources:
        # If the driver isn't found on your system PATH, Selenium
        # will automatically download it for you. Make sure there is no
        # chromedriver installed on your system
        service = Service()
        driver = webdriver.Chrome(service=service)

        driver.get(url)

        # give time to load javascript
        time.sleep(3)

        html_content = driver.page_source

        soup = BeautifulSoup(html_content, "html.parser")

        date_tag = soup.find("p", {"data-role": "date"})

        if not date_tag:
            msg = "The <p> tag with data-role='date' was not found on the page."
            raise DateTagNotFoundError(msg)

        last_updated = date_tag.get_text()

        # make downloaded_data folder if it doesn't exist yet
        if not downloaded_data_path.exists():
            downloaded_data_path.mkdir()

        # make data set folder if it doesn't exist yet
        ds_path = downloaded_data_path / ds_name
        if not ds_path.exists():
            ds_path.mkdir()

        # create unique directory
        last_updated_iso = datetime.strptime(last_updated, "%B %d, %Y").strftime(
            "%Y-%m-%d"
        )
        local_data_dir = ds_path / last_updated_iso

        if not local_data_dir.exists():
            local_data_dir.mkdir()

        # download and commit with datalad
        local_filename = local_data_dir / f"{ds_name}.zip"
        datalad.api.download_url(
            urls=url_download,
            message=f"Added {ds_name}",
            path=str(local_filename),
        )

        if local_filename.exists():
            print(f"Download => {local_filename.relative_to(root_path)}")
            # unzip data (only for new downloads)
            if local_filename.suffix == ".zip":
                try:
                    zipped_file = zipfile.ZipFile(str(local_filename), "r")
                    zipped_file.extractall(str(local_filename.parent))
                    print(f"Extracted {len(zipped_file.namelist())} files.")
                    zipped_file.close()
                    # os.remove(local_filename)
                # TODO Better error logging/visibilty
                except zipfile.BadZipFile:
                    print(
                        f"Error while trying to extract "
                        f"{local_filename.relative_to(root_path)}"
                    )
                except NotImplementedError:
                    print(
                        "Zip format not supported, " "please unzip on the command line."
                    )
            else:
                print(
                    f"Not attempting to extract "
                    f"{local_filename.relative_to(root_path)}."
                )
