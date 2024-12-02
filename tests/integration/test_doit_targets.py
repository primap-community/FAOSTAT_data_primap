import pytest
from doit.doit_cmd import DoitMain

from src.faostat_data_primap.helper.paths import root_path


@pytest.fixture
def change_to_project_root(monkeypatch):
    monkeypatch.chdir(root_path)


def test_doit_command(change_to_project_root, tmp_path):
    """
    Test a `doit` task programmatically.
    """
    save_path = tmp_path / "extracted_data"
    save_path.mkdir()

    # Command-line arguments for the doit task
    cmd_args = ["run", "read_data", f"save_path={save_path!s}", "run_id=2024"]

    # Run the doit command programmatically
    result = DoitMain().run(cmd_args)

    # Assert that the task ran successfully (return code 0)
    assert result == 0, f"doit task failed with return code: {result}"
