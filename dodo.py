"""
Define tasks to download and read the FAO data set.
"""
import datalad.api


def task_add_github_sibling():
    """
    Create github sibling after cloning from gin
    """

    def run_add_sibling():
        datalad.api.create_sibling_github(
            "primap-community/FAOSTAT_data_primap",
            name="github",
            existing="error",
            access_protocol="ssh",
            publish_depends="origin",
            private=False,
            dry_run=False,
            api="https://api.github.com",
        )

    return {"actions": [run_add_sibling]}


def task_download():
    """
    Download latest data
    """

    def datalad_run_download():
        datalad.api.run(
            cmd="python3 scripts/download_all_domains.py",
            outputs="downloaded_data",
        )

    return {"actions": [datalad_run_download]}


def task_read():
    """
    read data set
    """

    def read_dataset(save_path, run_id):
        print(f"Reading dataset for {save_path=} and {run_id=}")
        cmd = (
            f"python3 scripts/read_data_set.py "
            f"--save_path {save_path} --run_id {run_id}"
        )

        datalad.api.run(
            cmd=cmd,
            message="Read data set",
            outputs=f"{save_path}",
        )

    return {
        "actions": [read_dataset],
        "params": [
            {
                "name": "save_path",
                "short": "s",
                "long": "save_path",
                "default": "extracted_data",
                "help": "Path to save the data.",
            },
            {
                "name": "run_id",
                "long": "run_id",
                "short": "r",
                "default": "2024",
                "help": "Run identifier.",
            },
        ],
        "verbosity": 2,
    }
