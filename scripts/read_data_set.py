"""Read selected domains and versions."""
from pathlib import Path

import click

from faostat_data_primap.helper.definitions import domains_and_releases_to_read
from faostat_data_primap.helper.paths import (
    extracted_data_path,
)
from faostat_data_primap.read import (
    read_data,
)


@click.command()
@click.option("--run_id", default="2024", help="Configuration to run")
@click.option("--save_path", default=None, help="Where to save data in root directory.")
def run(run_id, save_path):
    """Prepare and run read data function"""
    if not save_path:
        save_path = extracted_data_path
    else:
        save_path = Path(save_path)
    read_data(
        domains_and_releases_to_read=domains_and_releases_to_read[run_id],
        save_path=save_path,
    )


if __name__ == "__main__":
    run()
