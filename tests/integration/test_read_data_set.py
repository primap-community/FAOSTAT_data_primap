import os
import subprocess
from pathlib import Path


def test_read_data_set(tmp_path):
    script_path = Path(__file__).parent.parent.parent / "scripts" / "read_data_set.py"

    # Build the command
    command = [
        "poetry",
        "run",
        "python3",
        str(script_path),
        "--save_path",
        str(tmp_path),
        "--run_id",
        "2024",
    ]

    # Run the command
    result = subprocess.run(command, capture_output=True, text=True, check=False)  # noqa: S603

    # Check the result
    assert result.returncode == 0, f"Script failed: {result.stderr}"

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
