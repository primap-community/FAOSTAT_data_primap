"""definitions like folders, mappings etc."""

from pathlib import Path

domains = {
    "farm_gate_emissions_crops": {
        "url_domain": "https://www.fao.org/faostat/en/#data/GCE",
        "url_download": "https://bulks-faostat.fao.org/production/Emissions_crops_E_All_Data.zip",
        "url_methodology": "https://files-faostat.fao.org/production/GCE/GCE_e.pdf",
    },
    "farm_gate_livestock": {
        "url_domain": "https://www.fao.org/faostat/en/#data/GLE",
        "url_download": "https://bulks-faostat.fao.org/production/Emissions_livestock_E_All_Data.zip",
        "url_methodology": "https://files-faostat.fao.org/production/GLE/GLE_e.pdf",
    },
    "farm_gate_agriculture_energy": {
        "url_domain": "https://www.fao.org/faostat/en/#data/GN",
        "url_download": "https://bulks-faostat.fao.org/production/Emissions_Agriculture_Energy_E_All_Data.zip",
        "url_methodology": "https://files-faostat.fao.org/production/GN/GN_2023Oct_Final.pdf",
    },
    "land_use_forests": {
        "url_domain": "https://www.fao.org/faostat/en/#data/GF",
        "url_download": "https://bulks-faostat.fao.org/production/Emissions_Land_Use_Forests_E_All_Data.zip",
        "url_methodology": "https://files-faostat.fao.org/production/GF/GF_e.pdf",
    },
    "land_use_fires": {
        "url_domain": "https://www.fao.org/faostat/en/#data/GI",
        "url_download": "https://bulks-faostat.fao.org/production/Emissions_Land_Use_Fires_E_All_Data.zip",
        "url_methodology": "https://files-faostat.fao.org/production/GI/GI_e.pdf",
    },
    "land_use_drained_organic_soils": {
        "url_domain": "https://www.fao.org/faostat/en/#data/GV",
        "url_download": "https://bulks-faostat.fao.org/production/Emissions_Drained_Organic_Soils_E_All_Data.zip",
        "url_methodology": "https://files-faostat.fao.org/production/GV/GV_e.pdf",
    },
    "pre_post_agricultural_production": {
        "url_domain": "https://www.fao.org/faostat/en/#data/GPP",
        "url_download": "https://bulks-faostat.fao.org/production/Emissions_Pre_Post_Production_E_All_Data.zip",
        "url_methodology": "https://files-faostat.fao.org/production/GPP/README_Methodological_Note.pdf",
    },
}


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
