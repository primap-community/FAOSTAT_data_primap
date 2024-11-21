import os

from src.faostat_data_primap.helper.paths import root_path
from src.faostat_data_primap.read import read_latest_data


def test_read_latest_data(tmp_path):
    # get the downloaded data from here
    downloaded_data_path = root_path / "downloaded_data"

    # read and save latest data
    read_latest_data(downloaded_data_path=downloaded_data_path, save_path=tmp_path)

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
