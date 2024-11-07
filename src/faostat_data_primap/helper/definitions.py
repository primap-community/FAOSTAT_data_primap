"""definitions like folders, mappings etc."""

from pathlib import Path


def get_root_path(root_indicator: str = ".git"):
    """
    Traverse up from the current script location to find the repository root.

    The root is defined by the presence of a root_indicator file or
    directory (e.g., '.git').

    Parameters
    ----------
        root_indicator
            A filename or directory name that indicates the root of the repository.

    Returns
    -------
    Path
        The path to the root directory of the repository.

    Raises
    ------
        RuntimeError: If the repository root cannot be found.
    """
    current_dir = Path(__file__).resolve().parent
    while current_dir != current_dir.root:
        if (current_dir / root_indicator).exists():
            return current_dir
        current_dir = current_dir.parent
    msg = f"Repository root with indicator '{root_indicator}' not found."
    raise RuntimeError(msg)


root_path = get_root_path()
code_path = root_path / "src" / "faostat_data_primap"
extracted_data_path = root_path / "extracted_data"
downloaded_data_path = root_path / "downloaded_data"
