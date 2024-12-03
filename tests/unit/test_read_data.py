import os

from src.faostat_data_primap.read import read_data


def test_read_data_one_domain(tmp_path):
    # read only one domain for the test
    domains_and_releases_to_read = (("land_use_fires", "2024-11-14"),)

    read_data(
        domains_and_releases_to_read=domains_and_releases_to_read, save_path=tmp_path
    )

    release_folder = os.listdir(tmp_path)

    # there should be one directory created
    assert len(release_folder) == 1
    # and it starts with "v" (the date changes with each release)
    assert release_folder[0].startswith("v")

    output_files = os.listdir(tmp_path / release_folder[0])
    # in the folder there should be three files
    assert len(output_files) == 3

    # a .yaml, .csv, and .nc file
    required_extensions = {"nc", "csv", "yaml"}
    file_extensions = {file.split(".")[-1] for file in output_files}
    assert required_extensions == file_extensions
