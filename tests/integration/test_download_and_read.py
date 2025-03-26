import os

from faostat_data_primap.download import download_all_domains
from faostat_data_primap.read import read_latest_data


# test the complete download and read process
# This will fail when there is a new release that does
# not have a corresponding configuration
def test_download_all_domains(tmp_path):
    downloaded_data_path = tmp_path / "downloaded_data"
    download_all_domains(downloaded_data_path=downloaded_data_path)

    expected_downloaded_domains = [
        "farm_gate_emissions_crops",
        "farm_gate_livestock",
        "farm_gate_agriculture_energy",
        "land_use_forests",
        "land_use_fires",
        "land_use_drained_organic_soils",
        "pre_post_agricultural_production",
    ]

    domains = []
    for domain in downloaded_data_path.iterdir():
        if domain.is_dir():
            domains.append(domain.name)
        for release in domain.iterdir():
            downloaded_data = os.listdir(release)
            # make sure we have at least one .csv, one .pdf and one .zip file
            assert [f for f in downloaded_data if f.endswith(".csv")]
            assert [f for f in downloaded_data if f.endswith(".pdf")]
            assert [f for f in downloaded_data if f.endswith(".zip")]

    assert sorted(expected_downloaded_domains) == sorted(domains)

    extracted_data_path = tmp_path / "extracted_data"

    # read and save latest data
    read_latest_data(
        downloaded_data_path_custom=downloaded_data_path, save_path=extracted_data_path
    )

    release_folder = os.listdir(extracted_data_path)

    # there should be one directory created
    assert len(release_folder) == 1
    # and it starts with "v" (the date changes with each release)
    assert release_folder[0].startswith("v")

    output_files = os.listdir(extracted_data_path / release_folder[0])

    # in the folder there should be three files
    assert len(output_files) == 6

    # a .yaml, .csv, and .nc file
    required_extensions = {"nc", "csv", "yaml"}
    file_extensions = {file.split(".")[-1] for file in output_files}
    assert required_extensions == file_extensions
