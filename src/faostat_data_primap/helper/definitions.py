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


def get_root_path(root_indicator: str = ".git") -> Path:
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
    while current_dir != Path(current_dir.root):
        if (current_dir / root_indicator).exists():
            return current_dir
        current_dir = current_dir.parent
    msg = f"Repository root with indicator '{root_indicator}' not found."
    raise RuntimeError(msg)


root_path = get_root_path()
code_path = root_path / "src" / "faostat_data_primap"
extracted_data_path = root_path / "extracted_data"
downloaded_data_path = root_path / "downloaded_data"

# data reading
areas_to_remove_base = [
    # We can aggregate these country groups ourselves if we need to
    "World",
    "Africa",
    "Eastern Africa",
    "Middle Africa",
    "Northern Africa",
    "Southern Africa",
    "Western Africa",
    "Americas",
    "Northern America",
    "Central America",
    "Caribbean",
    "South America",
    "Asia",
    "Central Asia",
    "Eastern Asia",
    "Southern Asia",
    "South-eastern Asia",
    "Western Asia",
    "Europe",
    "Eastern Europe",
    "Northern Europe",
    "Southern Europe",
    "Western Europe",
    "Oceania",
    "Australia and New Zealand",
    "Melanesia",
    "Micronesia",
    "Polynesia",
    "Least Developed Countries",
    "Land Locked Developing Countries",
    "Small Island Developing States",
    "Low Income Food Deficit Countries",
    "Net Food Importing Developing Countries",
    "Annex I countries",
    "Non-Annex I countries",
    "OECD",
]

read_config_all = {
    "farm_gate_agriculture_energy": {
        "2024-11-14": {
            # todo is NOFLAG the right choice?
            "filename": "Emissions_Agriculture_Energy_E_All_Data_NOFLAG.csv",
            # we don't need energy in Joule
            # todo maybe explicitly deleting elements is better
            "units_to_remove": ["TJ"],
            "areas_to_remove": [
                *areas_to_remove_base,
            ],
            "entity_mapping": {
                "Emissions (CO2)": "CO2",
                "Emissions (CH4)": "CH4",
                "Emissions (N2O)": "N2O",
            },
            "columns_to_drop": [
                "Element",
                "Element Code",
                "Item",
                "Item Code",
                "Area Code (M49)",
                "Area",
                "Area Code",
            ],
        }
    },
    "farm_gate_emissions_crops": {
        "2024-11-14": {
            "filename": "Emissions_crops_E_All_Data_NOFLAG.csv",
            "areas_to_remove": [
                *areas_to_remove_base,
                "European Union (27)",
                # This seems to be data for a Belgian province,
                # I don't think we need it
                "Belgium-Luxembourg",
                # I'm not sure if we can downscale these two
                "Serbia and Montenegro",
            ],
            "elements_to_remove": [
                # all these elements are not emissions
                "Crop residues (N content)",
                "Burning crop residues (Biomass burned, dry matter)",
                "Area harvested",
                "Nitrogen fertilizer content applied that leaches",
                "Nitrogen fertilizer content applied that volatilises",
                "Synthetic fertilizers (Agricultural use)",
            ],
            "entity_mapping": {
                "Crop residues (Emissions N2O)": "N2O",
                "Crop residues (Direct emissions N2O)": "N2O",
                "Crop residues (Indirect emissions N2O)": "N2O",
                "Burning crop residues (Emissions N2O)": "N2O",
                "Burning crop residues (Emissions CH4)": "CH4",
                "Rice cultivation (Emissions CH4)": "CH4",
                "Crops total (Emissions N2O)": "N2O",
                "Crops total (Emissions CH4)": "CH4",
                "Synthetic fertilizers (Emissions N2O)": "N2O",
                "Synthetic fertilizers (Direct emissions N2O)": "N2O",
                "Indirect emissions (N2O that leaches) (Synthetic fertilizers)": "N2O",
                "Indirect emissions (N2O that volatilises) (Synthetic fertilizers)": "N2O",
            },
            "columns_to_drop": [
                "Element",
                "Element Code",
                "Item",
                "Item Code",
                "Area Code (M49)",
                "Area",
                "Area Code",
                "Item Code (CPC)",
                "Source Code",
            ],
        }
    },
    "farm_gate_livestock": {
        "2024-11-14": {
            "filename": "Emissions_livestock_E_All_Data_NOFLAG.csv",
            "areas_to_remove": [
                *areas_to_remove_base,
                "Belgium-Luxembourg",
                "Serbia and Montenegro",
                "European Union (27)",
            ],
            "elements_to_remove": [
                "Stocks",  # number of animals
                "Manure management (manure treated, N content)",
                "Manure left on pasture (N content)",
                "Manure left on pasture that leaches (N content)",
                "Manure left on pasture that volatilises (N content)",
                "Manure applied to soils (N content)",
                "Manure applied to soils that leaches (N content)",
                "Manure applied to soils that volatilises (N content)",
            ],
            "entity_mapping": {
                # todo we could make this smarter and get the entity from the string
                "Livestock total (Emissions N2O)": "N2O",
                "Livestock total (Emissions CH4)": "CH4",
                "Enteric fermentation (Emissions CH4)": "CH4",
                "Manure management (Emissions CH4)": "CH4",
                "Manure management (Emissions N2O)": "N2O",
                "Manure management (Direct emissions N2O)": "N2O",
                "Manure management (Indirect emissions N2O)": "N2O",
                "Manure left on pasture (Emissions N2O)": "N2O",
                "Manure left on pasture (Direct emissions N2O)": "N2O",
                "Indirect emissions (N2O that leaches) (Manure on pasture)": "N2O",
                "Indirect emissions (N2O that volatilises) (Manure on pasture)": "N2O",
                "Manure left on pasture (Indirect emissions N2O)": "N2O",
                "Emissions (N2O) (Manure applied)": "N2O",
                "Manure applied to soils (Direct emissions N2O)": "N2O",
                "Indirect emissions (N2O that leaches) (Manure applied)": "N2O",
                "Indirect emissions (N2O that volatilises) (Manure applied)": "N2O",
                "Manure applied to soils (Indirect emissions N2O)": "N2O",
            },
            "columns_to_drop": [
                "Element",
                "Element Code",
                "Item",
                "Item Code",
                "Area Code (M49)",
                "Area",
                "Area Code",
                "Item Code (CPC)",
                "Source Code",
            ],
        }
    },
    "land_use_drained_organic_soils": {
        "2023-11-09": {
            "filename": "Emissions_Drained_Organic_Soils_E_All_Data_NOFLAG.csv",
            "areas_to_remove": [
                *areas_to_remove_base,
                "Belgium-Luxembourg",
                "Serbia and Montenegro",
                "European Union (27)",
                # check todo channel islands belong to UK
                "Channel Islands",
            ],
            "elements_to_remove": [
                "Area",
                # todo can we convert this into emissions?
                "Net stock change (C)",
            ],
            "entity_mapping": {
                "Emissions (N2O)": "N2O",
                "Emissions (CO2)": "CO2",
            },
            "columns_to_drop": [
                "Element",
                "Element Code",
                "Item",
                "Item Code",
                "Area Code (M49)",
                "Area",
                "Area Code",
                "Source Code",
            ],
        }
    },
    "land_use_fires": {
        "2023-11-09": {
            "filename": "Emissions_Land_Use_Fires_E_All_Data_NOFLAG.csv",
            "areas_to_remove": [
                *areas_to_remove_base,
                "Belgium-Luxembourg",
                "Serbia and Montenegro",
                "European Union (27)",
                # check todo channel islands belong to UK
                "Channel Islands",
            ],
            "elements_to_remove": ["Biomass burned (dry matter)", "Burned Area"],
            "entity_mapping": {
                "Emissions (CH4)": "CH4",
                "Emissions (N2O)": "N2O",
                "Emissions (CO2)": "CO2",
            },
            "columns_to_drop": [
                "Element",
                "Element Code",
                "Item",
                "Item Code",
                "Area Code (M49)",
                "Area",
                "Area Code",
                "Source Code",
            ],
        }
    },
    "land_use_forests": {
        "2024-11-14": {
            "filename": "Emissions_Land_Use_Forests_E_All_Data_NOFLAG.csv",
            "areas_to_remove": [
                *areas_to_remove_base,
                "Belgium-Luxembourg",
                "Serbia and Montenegro",
                "European Union (27)",
            ],
            "elements_to_remove": [
                "Area",
            ],
            "entity_mapping": {"Net emissions/removals (CO2) (Forest land)": "CO2"},
            "columns_to_drop": [
                "Element",
                "Element Code",
                "Item",
                "Item Code",
                "Area Code (M49)",
                "Area",
                "Area Code",
                "Source Code",
            ],
        }
    },
}
