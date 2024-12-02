"""
Define tasks to download and read the FAO data set.
"""
import datalad.api

from src.faostat_data_primap.helper.definitions import domains_and_releases_to_read


def get_output_folders(domains_and_releases_to_read):
    """Get the paths of folders where output files will be saved"""
    output_folders = []
    # todo remove hard coded key
    for domain, release in domains_and_releases_to_read["2024"]:
        # todo pathlib Path
        output_folders.append(f"downloaded_data/{domain}/{release}")
    return output_folders


def task_test_basic_target():
    """
    test
    """

    def do_nothing():
        pass

    return {"actions": [do_nothing]}


def task_test_download_target():
    """
    test datalad target
    """

    def datalad_run_download():
        datalad.api.run(cmd="python3 scripts/download_all_domains.py")

    return {"actions": [datalad_run_download]}


def task_read_data():
    """
    read data set
    """

    def read_dataset(save_path, run_id):
        output_folders = get_output_folders(domains_and_releases_to_read)

        cmd = (
            f"python3 scripts/read_data_set.py "
            f"--save_path {save_path} --run_id {run_id}"
        )

        datalad.api.run(
            cmd=cmd,
            message="Read data set",
            outputs=output_folders,
        )

    return {
        "actions": [read_dataset],
        "params": [
            {
                "name": "save_path",
                "short": "s",
                "default": "/extracted_data",
                "help": "Path to save the data.",
            },
            {
                "name": "run_id",
                "short": "r",
                "default": "2024",
                "help": "Run identifier.",
            },
        ],
        "verbosity": 2,
    }
