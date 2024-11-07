"""Downloads data from FAOSTAT website."""

import os
import zipfile
from datetime import datetime

import datalad.api
from helper.definitions import downloaded_data_path, root_path

if __name__ == "__main__":
    sources = [
        (
            "farm_gate_emissions_crops",
            "https://bulks-faostat.fao.org/production/Emissions_crops_E_All_Data.zip",
        ),
        (
            "farm_gate_livestock",
            "https://bulks-faostat.fao.org/production/Emissions_livestock_E_All_Data.zip",
        ),
        (
            "farm_gate_agriculture_energy",
            "https://bulks-faostat.fao.org/production/Emissions_Agriculture_Energy_E_All_Data.zip",
        ),
        (
            "land_use_forests",
            "https://bulks-faostat.fao.org/production/Emissions_Land_Use_Forests_E_All_Data.zip",
        ),
        (
            "land_use_fires",
            "https://bulks-faostat.fao.org/production/Emissions_Land_Use_Fires_E_All_Data.zip",
        ),
        (
            "land_use_drained_organic_soils",
            "https://bulks-faostat.fao.org/production/Emissions_Drained_Organic_Soils_E_All_Data.zip",
        ),
        (
            "pre_post_agricultural_production",
            "https://bulks-faostat.fao.org/production/Emissions_Pre_Post_Production_E_All_Data.zip",
        ),
    ]
    for ds_name, url in sources:
        # make downloaded_data folder if it doesn't exist yet
        if not downloaded_data_path.exists():
            downloaded_data_path.mkdir()

        # make data set folder if it doesn't exist yet
        ds_path = downloaded_data_path / ds_name
        if not ds_path.exists():
            ds_path.mkdir()

        # create unique directory
        # TODO unique name to be discussed
        today = datetime.today().strftime("%Y-%m-%d")
        local_data_dir = ds_path / today

        if not local_data_dir.exists():
            local_data_dir.mkdir()

        # download and commit with datalad
        local_filename = local_data_dir / "test.zip"
        datalad.api.download_url(
            urls=url,
            message=f"Added {ds_name}",
            path=str(local_filename),
        )

        # unzip
        if local_filename.exists():
            print(f"Download => {local_filename.relative_to(root_path)}")
            # unzip data (only for new downloads)
            if local_filename.suffix == ".zip":
                try:
                    zipped_file = zipfile.ZipFile(str(local_filename), "r")
                    zipped_file.extractall(str(local_filename.parent))
                    print(f"Extracted {len(zipped_file.namelist())} files.")
                    zipped_file.close()
                    os.remove(local_filename)
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

        # Questions:
        # * Push to datalad .zip and unzipped, or only unzipped?
        # * What unique directory name to use -
        # date or last updated from main data page?
        # * Pydoit to execute download script that stages files
        # and then push via command line
        # or is there another solution?
