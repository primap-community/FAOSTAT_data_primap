"""
Define tasks to download and read the FAO data set.
"""
import datalad.api


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
        datalad.api.run(cmd="python3 src/scripts/download_all_domains.py")

    return {"actions": [datalad_run_download]}
