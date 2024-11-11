"""Downloads all domain data sets from FAOSTAT website."""

import zipfile

import requests

from src.faostat_data_primap.download import get_html_content, get_last_updated_date
from src.faostat_data_primap.helper.definitions import downloaded_data_path, root_path

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

        local_filename = local_data_dir / f"{ds_name}.zip"

        response = requests.get(url_download, timeout=20)
        response.raise_for_status()

        # will overwrite existing file
        with open(local_filename, mode="wb") as file:
            file.write(response.content)

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
