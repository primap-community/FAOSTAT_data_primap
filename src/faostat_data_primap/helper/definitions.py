"""definitions like folders, mappings etc."""

from pathlib import Path

sources = [
    (
        "farm_gate_emissions_crops",
        "https://www.fao.org/faostat/en/#data/GCE",
        "https://bulks-faostat.fao.org/production/Emissions_crops_E_All_Data.zip",
    ),
    (
        "farm_gate_livestock",
        "https://www.fao.org/faostat/en/#data/GLE",
        "https://bulks-faostat.fao.org/production/Emissions_livestock_E_All_Data.zip",
    ),
    (
        "farm_gate_agriculture_energy",
        "https://www.fao.org/faostat/en/#data/GN",
        "https://bulks-faostat.fao.org/production/Emissions_Agriculture_Energy_E_All_Data.zip",
    ),
    (
        "land_use_forests",
        "https://www.fao.org/faostat/en/#data/GF",
        "https://bulks-faostat.fao.org/production/Emissions_Land_Use_Forests_E_All_Data.zip",
    ),
    (
        "land_use_fires",
        "https://www.fao.org/faostat/en/#data/GI",
        "https://bulks-faostat.fao.org/production/Emissions_Land_Use_Fires_E_All_Data.zip",
    ),
    (
        "land_use_drained_organic_soils",
        "https://www.fao.org/faostat/en/#data/GV",
        "https://bulks-faostat.fao.org/production/Emissions_Drained_Organic_Soils_E_All_Data.zip",
    ),
    (
        "pre_post_agricultural_production",
        "https://www.fao.org/faostat/en/#data/GPP",
        "https://bulks-faostat.fao.org/production/Emissions_Pre_Post_Production_E_All_Data.zip",
    ),
]


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
