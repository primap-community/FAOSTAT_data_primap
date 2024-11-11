"""Remove downloads for a particular date.

Files are saved in a folder named after the current date,
for example downloaded_data/farm_gate_agriculture_energy/2024-11-07
This script deletes all files in such a folder. It is
useful when testing downloads. Needs to be updated with the directory
structure or maybe can be deleted altogether later.
"""

import os

import click

from faostat_data_primap.helper.definitions import downloaded_data_path


@click.command()
@click.option(
    "--date",
    help="The day on which the data to be deleted was downloaded",
    default="2024-11-11",
)
def run(date: str):
    """
    Delete all downloaded files for one day.
    """
    domains = os.listdir(downloaded_data_path)

    for domain in domains:
        path_to_files = downloaded_data_path / domain / date
        files_to_delete = os.listdir(path_to_files)

        for file in files_to_delete:
            path_to_file = path_to_files / file
            os.remove(path_to_file)


if __name__ == "__main__":
    run()
