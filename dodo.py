"""
Define tasks to download and read the FAO data set.
"""
import datalad.api

# we need this for the download script
# def get_output_folders(domains_and_releases_to_read):
#     """Get the paths of folders where output files will be saved"""
#     output_folders = []
#     # todo remove hard coded key
#     for domain, release in domains_and_releases_to_read["2024"]:
#         # todo pathlib Path
#         output_folders.append(f"downloaded_data/{domain}/{release}")
#     return output_folders


def task_test_basic_target():
    """
    test
    """

    def do_nothing():
        pass

    return {"actions": [do_nothing]}


def task_download():
    """
    test datalad target
    """

    def datalad_run_download():
        datalad.api.run(
            cmd="python3 scripts/download_all_domains.py", outputs="downloaded_data"
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
