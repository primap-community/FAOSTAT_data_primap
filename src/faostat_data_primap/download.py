"""Downloads data from FAOSTAT website."""
# links we will need:
# download farm gate
# https://bulks-faostat.fao.org/production/Emissions_crops_E_All_Data.zip
# https://bulks-faostat.fao.org/production/Emissions_livestock_E_All_Data.zip
# https://bulks-faostat.fao.org/production/Emissions_Agriculture_Energy_E_All_Data.zip
# download land use and change
# https://bulks-faostat.fao.org/production/Emissions_Land_Use_Forests_E_All_Data.zip
# https://bulks-faostat.fao.org/production/Emissions_Land_Use_Fires_E_All_Data.zip
# https://bulks-faostat.fao.org/production/Emissions_Drained_Organic_Soils_E_All_Data.zip
# download pre and post agricultural production
# https://bulks-faostat.fao.org/production/Emissions_Pre_Post_Production_E_All_Data.zip

import shutil
import time
import zipfile

import requests
from helper.definitions import downloaded_data_path, root_path
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

if __name__ == "__main__":
    # set options for headless mode
    profile_path = ".firefox"
    options = Options()
    # options.add_argument('-headless')

    # create profile for headless mode and automatic downloading
    options.set_preference("profile", profile_path)
    options.set_preference("browser.download.folderList", 2)

    # set up selenium driver
    driver = Firefox(options=options)
    # visit the main data page once to create cookies
    driver.get("https://www.fao.org/faostat/en/#data")

    # wait a bit for the website to load before we get the cokkies
    time.sleep(1)

    # get the session id cookie
    cookies_selenium = driver.get_cookies()
    cookies = {}
    for cookie in cookies_selenium:
        cookies[cookie["name"]] = cookie["value"]

    dataset = "emissions_crops"
    url = "https://bulks-faostat.fao.org/production/Emissions_crops_E_All_Data.zip"

    if not downloaded_data_path.exists():
        downloaded_data_path.mkdir()

    local_filename = downloaded_data_path / dataset / "insert_uniqie_identifier"

    if not local_filename.parent.exists():
        local_filename.parent.mkdir()

    # if local_filename.exists() :
    #     # check file size. if 210 or 212 bytes it's the error page
    #     if Path(local_filename).stat().st_size in error_file_sizes :
    #         # found the error page. delete file
    #         os.remove(local_filename)

    # now we have removed error pages, so a present file should not be overwritten
    if (not local_filename.exists()) and (not local_filename.is_symlink()):
        i = 0  # reset counter
        while not local_filename.exists() and i < 10:  # noqa: PLR2004
            # for i = 0 and i = 5 try to get a new session ID
            if i in (1, 5):
                driver = Firefox(options=options)

                # visit the main data page once to create cookies
                driver.get(url)
                time.sleep(20)

                # get the session id cookie
                cookies_selenium = driver.get_cookies()
                cookies = {}
                for cookie in cookies_selenium:
                    cookies[cookie["name"]] = cookie["value"]

            r = requests.get(url, stream=True, cookies=cookies, timeout=120)
            with open(str(local_filename), "wb") as f:
                shutil.copyfileobj(r.raw, f)

        if local_filename.exists():
            print(f"Download => {local_filename.relative_to(root_path)}")
            # unzip data (only for new downloads)
            if local_filename.suffix == ".zip":
                try:
                    zipped_file = zipfile.ZipFile(str(local_filename), "r")
                    zipped_file.extractall(str(local_filename.parent))
                    print(f"Extracted {len(zipped_file.namelist())} files.")
                    zipped_file.close()
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
        else:
            print(f"Failed to download {local_filename.relative_to(root_path)}")

    driver.close()
