"""definitions like folders, mappings etc."""

from typing import Any

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

# TODO would be a nice to have a type hint here
read_config_all: Any = {
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
            "category_mapping_item_element": {
                "Electricity - Emissions (CO2)": "2.B",
                "Electricity - Emissions (CH4)": "2.B",
                "Electricity - Emissions (N2O)": "2.B",
                "Total Energy - Emissions (CO2)": "2",
                "Total Energy - Emissions (CH4)": "2",
                "Total Energy - Emissions (N2O)": "2",
                "Petroleum products - Emissions (CO2)": "2.E",
                "Petroleum products - Emissions (CH4)": "2.E",
                "Petroleum products - Emissions (N2O)": "2.E",
                "Natural gas - Emissions (CO2)": "2.A",
                "Natural gas - Emissions (CH4)": "2.A",
                "Natural gas - Emissions (N2O)": "2.A",
                "Coal - Emissions (CO2)": "2.C",
                "Coal - Emissions (CH4)": "2.C",
                "Coal - Emissions (N2O)": "2.C",
                "Heat - Emissions (CO2)": "2.D",
                "Heat - Emissions (CH4)": "2.D",
                "Heat - Emissions (N2O)": "2.D",
            },
            "items-elements_to_remove": [
                "Total Energy (excl.eletricity & heat) - Emissions (CO2)",
                "Total Energy (excl.eletricity & heat) - Emissions (CH4)",
                "Total Energy (excl.eletricity & heat) - Emissions (N2O)",
            ],
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
            "category_mapping_item_element": {
                "Barley - Crop residues (Emissions N2O)": "1.A.5.a",
                "Barley - Crop residues (Direct emissions N2O)": "1.A.5.a.i",
                "Barley - Crop residues (Indirect emissions N2O)": "1.A.5.a.ii",
                "Maize (corn) - Crop residues (Emissions N2O)": "1.A.6.a",
                "Maize (corn) - Crop residues (Direct emissions N2O)": "1.A.6.a.i",
                "Maize (corn) - Crop residues (Indirect emissions N2O)": "1.A.6.a.ii",
                "Maize (corn) - Burning crop residues (Emissions N2O)": "1.A.6.b",
                "Maize (corn) - Burning crop residues (Emissions CH4)": "1.A.6.b",
                "Sugar cane - Crop residues (Emissions N2O)": "1.A.7.a",
                "Sugar cane - Burning crop residues (Emissions N2O)": "1.A.7.b",
                "Sugar cane - Burning crop residues (Emissions CH4)": "1.A.7.b",
                "Millet - Crop residues (Emissions N2O)": "1.A.4.a",
                "Millet - Crop residues (Direct emissions N2O)": "1.A.4.a.i",
                "Millet - Crop residues (Indirect emissions N2O)": "1.A.4.a.ii",
                "Potatoes - Crop residues (Emissions N2O)": "1.A.3.a",
                "Potatoes - Crop residues (Direct emissions N2O)": "1.A.3.a.i",
                "Potatoes - Crop residues (Indirect emissions N2O)": "1.A.3.a.ii",
                "Rice - Crop residues (Emissions N2O)": "1.A.2.a",
                "Rice - Crop residues (Direct emissions N2O)": "1.A.2.a.i",
                "Rice - Crop residues (Indirect emissions N2O)": "1.A.2.a.ii",
                "Rice - Burning crop residues (Emissions N2O)": "1.A.2.b",
                "Rice - Burning crop residues (Emissions CH4)": "1.A.2.b",
                "Rice - Rice cultivation (Emissions CH4)": "1.A.2.c",
                "Wheat - Crop residues (Emissions N2O)": "1.A.1.a",
                "Wheat - Crop residues (Direct emissions N2O)": "1.A.1.a.i",
                "Wheat - Crop residues (Indirect emissions N2O)": "1.A.1.a.ii",
                "Wheat - Burning crop residues (Emissions N2O)": "1.A.1.b",
                "Wheat - Burning crop residues (Emissions CH4)": "1.A.1.b",
                "All Crops - Crops total (Emissions N2O)": "1.A",
                "All Crops - Crops total (Emissions CH4)": "1.A",
                (
                    "Nutrient nitrogen N (total) - Synthetic "
                    "fertilizers (Emissions N2O)"
                ): "1.B",
                (
                    "Nutrient nitrogen N (total) - "
                    "Synthetic fertilizers (Direct emissions N2O)"
                ): "1.B.1",
                (
                    "Nutrient nitrogen N (total) - "
                    "Indirect emissions (N2O that leaches) "
                    "(Synthetic fertilizers)"
                ): "1.B.2.b",
                (
                    "Nutrient nitrogen N (total) - "
                    "Indirect emissions (N2O that volatilises) "
                    "(Synthetic fertilizers)"
                ): "1.B.2.a",
                "Beans, dry - Crop residues (Emissions N2O)": "1.A.8.a",
                "Beans, dry - Crop residues (Direct emissions N2O)": "1.A.8.a.i",
                "Beans, dry - Crop residues (Indirect emissions N2O)": "1.A.8.a.ii",
                "Oats - Crop residues (Emissions N2O)": "1.A.9.a",
                "Oats - Crop residues (Direct emissions N2O)": "1.A.9.a.i",
                "Oats - Crop residues (Indirect emissions N2O)": "1.A.9.a.ii",
                "Rye - Crop residues (Emissions N2O)": "1.A.10.a",
                "Rye - Crop residues (Direct emissions N2O)": "1.A.10.a.i",
                "Rye - Crop residues (Indirect emissions N2O)": "1.A.10.a.ii",
                "Sorghum - Crop residues (Emissions N2O)": "1.A.11.a",
                "Sorghum - Crop residues (Direct emissions N2O)": "1.A.11.a.i",
                "Sorghum - Crop residues (Indirect emissions N2O)": "1.A.11.a.ii",
                "Soya beans - Crop residues (Emissions N2O)": "1.A.12.a",
                "Soya beans - Crop residues (Direct emissions N2O)": "1.A.12.a.i",
                "Soya beans - Crop residues (Indirect emissions N2O)": "1.A.12.a.ii",
                "Maize (corn) - Crops total (Emissions N2O)": "1.A.6",
                "Maize (corn) - Crops total (Emissions CH4)": "1.A.6",
                "Sugar cane - Crops total (Emissions N2O)": "1.A.7",
                "Sugar cane - Crops total (Emissions CH4)": "1.A.7",
                "Rice - Crops total (Emissions N2O)": "1.A.2",
                "Rice - Crops total (Emissions CH4)": "1.A.2",
                "Wheat - Crops total (Emissions N2O)": "1.A.1",
                "Wheat - Crops total (Emissions CH4)": "1.A.1",
            },
            "items-elements_to_remove": [
                "All Crops - Crop residues (Emissions N2O)",
                "All Crops - Crop residues (Direct emissions N2O)",
                "All Crops - Crop residues (Indirect emissions N2O)",
                "All Crops - Burning crop residues (Emissions N2O)",
                "All Crops - Burning crop residues (Emissions CH4)",
            ],
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
            "items_to_remove": [
                # we don't need aggregates
                "Camels and Llamas",
                "Cattle",  # dairy and non-dairy
                # mistake by FAO, should be "Mules, hinnies, and asses"
                "Mules and Asses",
                "Sheep and Goats",
                "Swine",  # breeding and market
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
                # TODO ?
                # sum of direct and direct manure management emissions
                # would add another level in the category tree, but
                # is not needed (see miro)
                # "Manure management (Emissions N2O)",
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
            "category_mapping_item": {
                "All Animals": "3",
                "Asses": "3.A",
                "Camels": "3.B",
                "Cattle, dairy": "3.C",
                "Cattle, non-dairy": "3.D",
                "Chickens, broilers": "3.E",
                "Chickens, layers": "3.F",
                "Goats": "3.G",
                "Horses": "3.H",
                "Mules and hinnies": "3.I",
                "Sheep": "3.J",
                "Llamas": "3.K",
                "Chickens": "3.L",
                "Poultry Birds": "3.M",
                "Buffalo": "3.N",
                "Ducks": "3.O",
                "Swine, breeding": "3.P",
                "Swine, market": "3.Q",
                "Turkeys": "3.R",
            },
            "category_mapping_element": {
                "Livestock total (Emissions N2O)": "",
                "Livestock total (Emissions CH4)": "",
                "Enteric fermentation (Emissions CH4)": ".4",
                "Manure management (Emissions CH4)": ".1.a",
                # TODO we need to aggregate 3.X.1 for CH4
                "Manure management (Emissions N2O)": ".1",
                "Manure management (Direct emissions N2O)": ".1.b",
                "Manure management (Indirect emissions N2O)": ".1.c",
                "Manure left on pasture (Emissions N2O)": ".2",
                "Manure left on pasture (Direct emissions N2O)": ".2.a",
                "Indirect emissions (N2O that leaches) (Manure on pasture)": ".2.b.i",
                (
                    "Indirect emissions (N2O that volatilises) " "(Manure on pasture)"
                ): ".2.b.ii",
                "Manure left on pasture (Indirect emissions N2O)": ".2.b",
                "Emissions (N2O) (Manure applied)": ".3",
                "Manure applied to soils (Direct emissions N2O)": ".3.a",
                ("Indirect emissions (N2O that leaches) " "(Manure applied)"): ".3.b.i",
                "Indirect emissions (N2O that volatilises) (Manure applied)": ".3.b.ii",
                "Manure applied to soils (Indirect emissions N2O)": ".3.b",
            },
            "items-elements_to_remove": [
                # we only keep All animals total CH4 and total N2O
                "All Animals - Enteric fermentation (Emissions CH4)",
                "All Animals - Manure management (Emissions CH4)",
                "All Animals - Manure management (Direct emissions N2O)",
                "All Animals - Manure management (Indirect emissions N2O)",
                "All Animals - Manure left on pasture (Emissions N2O)",
                "All Animals - Manure left on pasture (Direct emissions N2O)",
                (
                    "All Animals - Indirect emissions (N2O that leaches) "
                    "(Manure on pasture)"
                ),
                (
                    "All Animals - Indirect emissions (N2O that volatilises) "
                    "(Manure on pasture)"
                ),
                "All Animals - Manure left on pasture (Indirect emissions N2O)",
                "All Animals - Emissions (N2O) (Manure applied)",
                "All Animals - Manure applied to soils (Direct emissions N2O)",
                "All Animals - Indirect emissions (N2O that leaches) (Manure applied)",
                (
                    "All Animals - Indirect emissions (N2O that volatilises) "
                    "(Manure applied)"
                ),
                "All Animals - Manure applied to soils (Indirect emissions N2O)",
                "All Animals - Manure management (Emissions N2O)",
            ],
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
                # "Belgium-Luxembourg",
                # "Serbia and Montenegro",
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

# TODO maybe this should live somewhere else?
# Definition of the domains and releases to be read
domains_and_releases_to_read = {
    "2024": [
        ("farm_gate_agriculture_energy", "2024-11-14"),
        ("farm_gate_emissions_crops", "2024-11-14"),
        ("farm_gate_livestock", "2024-11-14"),
        ("land_use_drained_organic_soils", "2024-11-14"),
        ("land_use_fires", "2024-11-14"),
        ("land_use_forests", "2024-11-14"),
        ("pre_post_agricultural_production", "2024-11-14"),
    ]
}
