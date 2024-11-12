"""Remove all downloads.

This script deletes all downloaded and unzipped files. It is
useful for testing purposes. Needs to be updated with the directory
structure or maybe can be deleted altogether later.
"""

import os

# import click
from faostat_data_primap.helper.definitions import downloaded_data_path


def run():
    """
    Delete all downloaded files for all domains and all releases
    """
    domains = [
        d
        for d in os.listdir(downloaded_data_path)
        if os.path.isdir(downloaded_data_path / d)
    ]

    for domain in domains:
        path_to_releases = downloaded_data_path / domain
        releases = [
            d
            for d in os.listdir(path_to_releases)
            if os.path.isdir(path_to_releases / d)
        ]

        for release in releases:
            path_to_files = downloaded_data_path / domain / release
            files_to_delete = os.listdir(path_to_files)

            for file in files_to_delete:
                path_to_file = path_to_files / file
                os.remove(path_to_file)


if __name__ == "__main__":
    run()
