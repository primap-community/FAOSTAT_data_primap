"""definitions like folders, mappings etc."""

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

areas_to_remove_base = [
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
    "Europe, Northern America, Australia and New Zealand",
]

read_config_all = {
    "farm_gate_agriculture_energy": {
        "2024-11-14": {
            "filename": "Emissions_Agriculture_Energy_E_All_Data_NOFLAG.csv",
            "areas_to_remove": [
                *areas_to_remove_base,
            ],
            "elements_to_remove": ["Energy use in agriculture"],
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
            ],
            "elements_to_remove": [
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
                (
                    "Indirect emissions (N2O that volatilises) "
                    "(Synthetic fertilizers)"
                ): "N2O",
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
            ],
            "elements_to_remove": [
                "Area",
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
        },
        "2024-11-14": {
            "filename": "Emissions_Drained_Organic_Soils_E_All_Data_NOFLAG.csv",
            "areas_to_remove": [
                *areas_to_remove_base,
                "Belgium-Luxembourg",
                "Serbia and Montenegro",
                "European Union (27)",
            ],
            "elements_to_remove": [
                "Area",
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
        },
    },
    "land_use_fires": {
        "2023-11-09": {
            "filename": "Emissions_Land_Use_Fires_E_All_Data_NOFLAG.csv",
            "areas_to_remove": [
                *areas_to_remove_base,
                "European Union (27)",
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
        },
        "2024-11-14": {
            "filename": "Emissions_Land_Use_Fires_E_All_Data_NOFLAG.csv",
            "areas_to_remove": [
                *areas_to_remove_base,
                "European Union (27)",
            ],
            "elements_to_remove": [
                "Burning crop residues (Biomass burned, dry matter)",
                "Burned Area",
            ],
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
        },
    },
    "land_use_forests": {
        "2024-11-14": {
            "filename": "Emissions_Land_Use_Forests_E_All_Data_NOFLAG.csv",
            "areas_to_remove": [
                *areas_to_remove_base,
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
    "pre_post_agricultural_production": {
        "2023-11-09": {
            "filename": "Emissions_Pre_Post_Production_E_All_Data_NOFLAG.csv",
            "areas_to_remove": [
                *areas_to_remove_base,
                "European Union (27)",
            ],
            "elements_to_remove": [
                "Energy Use (Total)",
                "Energy Use (Electricity)",
                "Energy Use (Natural Gas, including LNG)",
                "Energy Use (Heat)",
                "Energy Use (Coal)",
            ],
            "entity_mapping": {
                "Emissions (CO2)": "CO2",
                "Emissions (CO2eq) (AR5)": "KYOTOGHG (AR5GWP100)",
                "Emissions (CH4)": "CH4",
                "Emissions (N2O)": "N2O",
                "Emissions (CO2eq) from F-gases (AR5)": "FGASES (AR5GWP100)",
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
        },
        "2024-11-14": {
            "filename": "Emissions_Pre_Post_Production_E_All_Data_NOFLAG.csv",
            "areas_to_remove": [
                *areas_to_remove_base,
                "European Union (27)",
            ],
            "elements_to_remove": [
                "Energy Use (Total)",
                "Energy Use (Electricity)",
                "Energy Use (Natural Gas, including LNG)",
                "Energy Use (Heat)",
                "Energy Use (Coal)",
            ],
            "entity_mapping": {
                "Emissions (CO2)": "CO2",
                "Emissions (CO2eq) (AR5)": "KYOTOGHG (AR5GWP100)",
                "Emissions (CH4)": "CH4",
                "Emissions (N2O)": "N2O",
                "Emissions (CO2eq) from F-gases (AR5)": "FGASES (AR5GWP100)",
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
        },
    },
    "replace_units": {
        "KYOTOGHG (AR5GWP100) * kt/ year": "CO2 * kt / year",
        "FGASES (AR5GWP100) * kt/ year": "CO2 * kt/ year",
    },
}

config_to_if = {
    "coords_cols": {
        "area": "country (ISO3)",
        "unit": "Unit",
        "entity": "entity",
        "source": "Source",
        "category": "category",
    },
    "coords_terminologies": {"area": "ISO3", "category": "FAOSTAT", "scenario": "FAO"},
    "coords_value_mapping": {},
    "filter_keep": {},
    "filter_remove": {},
    "meta_data": {
        "references": "https://www.fao.org/faostat",
        "rights": "Creative Commons Attribution-4.0 International licence (CC BY 4.0)",
        "contact": "daniel.busch@climate-resource.com",
        "title": "Agrifood systems emissions",
        "comment": (
            "Published by Food and Agriculture Organization of the "
            "United Nations (FAO), converted to PRIMAP2 format by "
            "Daniel Busch"
        ),
        "institution": ("Food and Agriculture Organization of the United Nations"),
    },
}
