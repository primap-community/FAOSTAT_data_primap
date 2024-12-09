"""
Temporary version of FAO categorisation.

Will be imported from climate categories when the FAO categorisation is finished.
"""
spec = {
    "name": "FAO",
    "title": (
        "Food and Agriculture Organization of the United "
        "Nations (FAO) FAOSTAT data set categorisation"
    ),
    "comment": "Needed to add FAOSTAT data to PRIMAP-hist",
    "references": "",
    "institution": "FAO",
    "hierarchical": True,
    "last_update": "2024-12-10",
    "version": "2024",
    "total_sum": True,
    "canonical_top_level_category": "0",
    "categories": {
        "0": {
            "title": "Total",
            "comment": "All emissions and removals",
            "children": [["1", "2", "3", "4", "5", "6", "7"]],
        },
        "1": {
            "title": "Crops",
            "comment": "Crops",
            "info": {"gases": ["CH4", "N2O"]},
            "children": [["1.A", "1.B"]],
        },
        "2": {
            "title": "Energy use in agriculture",
            "comment": "Energy use in agriculture",
            "info": {"gases": ["CH4", "N2O", "CO2"]},
            "children": [["2.A", "2.B", "2.C", "2.D", "2.E"]],
        },
        "3": {
            "title": "Livestock",
            "comment": "Livestock",
            "info": {"gases": ["CH4", "N2O"]},
            "children": [
                [
                    "3.A",
                    "3.B",
                    "3.C",
                    "3.D",
                    "3.E",
                    "3.F",
                    "3.G",
                    "3.H",
                    "3.I",
                    "3.J",
                    "3.K",
                    "3.L",
                    "3.M",
                    "3.N",
                    "3.O",
                    "3.P",
                    "3.Q",
                    "3.R",
                ]
            ],
        },
        "1.A": {
            "title": "All crops",
            "comment": "All crops",
            "info": {"gases": ["CH4", "N2O"]},
            "children": [
                [
                    "1.A.1",
                    "1.A.10",
                    "1.A.11",
                    "1.A.12",
                    "1.A.2",
                    "1.A.3",
                    "1.A.4",
                    "1.A.5",
                    "1.A.6",
                    "1.A.7",
                    "1.A.8",
                    "1.A.9",
                ]
            ],
        },
        "1.A.1": {
            "title": "Wheat",
            "comment": "Wheat",
            "info": {"gases": ["CH4", "N2O"]},
            "children": [["1.A.1.a", "1.A.1.b"]],
        },
        "1.A.1.a.i": {
            "title": "Wheat crop residues direct emissions",
            "comment": "Wheat crop residues direct emissions",
            "info": {"gases": ["N2O"]},
        },
        "1.A.1.a.ii": {
            "title": "Wheat crop residues indirect emissions",
            "comment": "Wheat crop residues indirect emissions",
            "info": {"gases": ["N2O"]},
        },
        "1.A.1.a": {
            "title": "Wheat crop residues",
            "comment": "Wheat crop residues",
            "info": {"gases": ["N2O"]},
            "children": [["1.A.1.a.i", "1.A.1.a.ii"]],
        },
        "1.A.1.b": {
            "title": "Wheat burning crop residues",
            "comment": "Wheat burning crop residues",
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.2": {
            "title": "Rice",
            "comment": "Rice",
            "info": {"gases": ["CH4", "N2O"]},
            "children": [["1.A.2.a", "1.A.2.b", "1.A.2.c"]],
        },
        "1.A.2.a.i": {
            "title": "Rice crop residues direct emissions",
            "comment": "Rice crop residues direct emissions",
            "info": {"gases": ["N2O"]},
        },
        "1.A.2.a.ii": {
            "title": "Rice crop residues indirect emissions",
            "comment": "Rice crop residues indirect emissions",
            "info": {"gases": ["N2O"]},
        },
        "1.A.2.a": {
            "title": "Rice crop residues",
            "comment": "Rice crop residues",
            "info": {"gases": ["N2O"]},
            "children": [["1.A.2.a.i", "1.A.2.a.ii"]],
        },
        "1.A.2.b": {
            "title": "Rice burning crop residues",
            "comment": "Rice burning crop residues",
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.2.c": {
            "title": "Rice cultivation",
            "comment": "Rice cultivation",
            "info": {"gases": ["CH4"]},
        },
        "1.A.3": {
            "title": "Potatoes",
            "comment": "Potatoes",
            "info": {"gases": "N2O"},
            "children": [["1.A.3.a"]],
        },
        "1.A.3.a.i": {
            "title": "Potatoes crop residues direct emissions",
            "comment": "Potatoes crop residues direct emissions",
            "info": {"gases": ["N2O"]},
        },
        "1.A.3.a.ii": {
            "title": "Potatoes crop residues indirect emissions",
            "comment": "Potatoes crop residues indirect emissions",
            "info": {"gases": ["N2O"]},
        },
        "1.A.3.a": {
            "title": "Potatoes crop residues",
            "comment": "Potatoes crop residues",
            "info": {"gases": ["N2O"]},
            "children": [["1.A.3.a.i", "1.A.3.a.ii"]],
        },
        "1.A.4": {
            "title": "Millet",
            "comment": "Millet",
            "info": {"gases": "N2O"},
            "children": [["1.A.4.a"]],
        },
        "1.A.4.a.i": {
            "title": "Millet crop residues direct emissions",
            "comment": "Millet crop residues direct emissions",
            "info": {"gases": ["N2O"]},
        },
        "1.A.4.a.ii": {
            "title": "Millet crop residues indirect emissions",
            "comment": "Millet crop residues indirect emissions",
            "info": {"gases": ["N2O"]},
        },
        "1.A.4.a": {
            "title": "Millet crop residues",
            "comment": "Millet crop residues",
            "info": {"gases": ["N2O"]},
            "children": [["1.A.4.a.i", "1.A.4.a.ii"]],
        },
        "1.A.5": {
            "title": "Barley",
            "comment": "Barley",
            "info": {"gases": "N2O"},
            "children": [["1.A.5.a"]],
        },
        "1.A.5.a.i": {
            "title": "Barley crop residues direct emissions",
            "comment": "Barley crop residues direct emissions",
            "info": {"gases": ["N2O"]},
        },
        "1.A.5.a.ii": {
            "title": "Barley crop residues indirect emissions",
            "comment": "Barley crop residues indirect emissions",
            "info": {"gases": ["N2O"]},
        },
        "1.A.5.a": {
            "title": "Barley crop residues",
            "comment": "Barley crop residues",
            "info": {"gases": ["N2O"]},
            "children": [["1.A.5.a.i", "1.A.5.a.ii"]],
        },
        "1.A.6": {
            "title": "Maize (corn)",
            "comment": "Maize (corn)",
            "info": {"gases": ["CH4", "N2O"]},
            "children": [["1.A.6.a", "1.A.6.b"]],
        },
        "1.A.6.a.i": {
            "title": "Maize (corn) crop residues direct emissions",
            "comment": "Maize (corn) crop residues direct emissions",
            "info": {"gases": ["N2O"]},
        },
        "1.A.6.a.ii": {
            "title": "Maize (corn) crop residues indirect emissions",
            "comment": "Maize (corn) crop residues indirect emissions",
            "info": {"gases": ["N2O"]},
        },
        "1.A.6.a": {
            "title": "Maize (corn) crop residues",
            "comment": "Maize (corn) crop residues",
            "info": {"gases": ["N2O"]},
            "children": [["1.A.6.a.i", "1.A.6.a.ii"]],
        },
        "1.A.6.b": {
            "title": "Maize (corn) burning crop residues",
            "comment": "Maize (corn) burning crop residues",
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.7": {
            "title": "Sugar cane",
            "comment": "Sugar cane",
            "info": {"gases": ["CH4", "N2O"]},
            "children": [["1.A.7.a", "1.A.7.b"]],
        },
        "1.A.7.a.i": {
            "title": "Sugar cane crop residues direct emissions",
            "comment": "Sugar cane crop residues direct emissions",
            "info": {"gases": ["N2O"]},
        },
        "1.A.7.a.ii": {
            "title": "Sugar cane crop residues indirect emissions",
            "comment": "Sugar cane crop residues indirect emissions",
            "info": {"gases": ["N2O"]},
        },
        "1.A.7.a": {
            "title": "Sugar cane crop residues",
            "comment": "Sugar cane crop residues",
            "info": {"gases": ["N2O"]},
            "children": [["1.A.7.a.i", "1.A.7.a.ii"]],
        },
        "1.A.7.b": {
            "title": "Sugar cane burning crop residues",
            "comment": "Sugar cane burning crop residues",
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.8": {
            "title": "Beans, dry",
            "comment": "Beans, dry",
            "info": {"gases": "N2O"},
            "children": [["1.A.8.a"]],
        },
        "1.A.8.a.i": {
            "title": "Beans, dry crop residues direct emissions",
            "comment": "Beans, dry crop residues direct emissions",
            "info": {"gases": ["N2O"]},
        },
        "1.A.8.a.ii": {
            "title": "Beans, dry crop residues indirect emissions",
            "comment": "Beans, dry crop residues indirect emissions",
            "info": {"gases": ["N2O"]},
        },
        "1.A.8.a": {
            "title": "Beans, dry crop residues",
            "comment": "Beans, dry crop residues",
            "info": {"gases": ["N2O"]},
            "children": [["1.A.8.a.i", "1.A.8.a.ii"]],
        },
        "1.A.9": {
            "title": "Oats",
            "comment": "Oats",
            "info": {"gases": "N2O"},
            "children": [["1.A.9.a"]],
        },
        "1.A.9.a.i": {
            "title": "Oats crop residues direct emissions",
            "comment": "Oats crop residues direct emissions",
            "info": {"gases": ["N2O"]},
        },
        "1.A.9.a.ii": {
            "title": "Oats crop residues indirect emissions",
            "comment": "Oats crop residues indirect emissions",
            "info": {"gases": ["N2O"]},
        },
        "1.A.9.a": {
            "title": "Oats crop residues",
            "comment": "Oats crop residues",
            "info": {"gases": ["N2O"]},
            "children": [["1.A.9.a.i", "1.A.9.a.ii"]],
        },
        "1.A.10": {
            "title": "Rye",
            "comment": "Rye",
            "info": {"gases": "N2O"},
            "children": [["1.A.10.a"]],
        },
        "1.A.10.a.i": {
            "title": "Rye crop residues direct emissions",
            "comment": "Rye crop residues direct emissions",
            "info": {"gases": ["N2O"]},
        },
        "1.A.10.a.ii": {
            "title": "Rye crop residues indirect emissions",
            "comment": "Rye crop residues indirect emissions",
            "info": {"gases": ["N2O"]},
        },
        "1.A.10.a": {
            "title": "Rye crop residues",
            "comment": "Rye crop residues",
            "info": {"gases": ["N2O"]},
            "children": [["1.A.10.a.i", "1.A.10.a.ii"]],
        },
        "1.A.11": {
            "title": "Sorghum",
            "comment": "Sorghum",
            "info": {"gases": "N2O"},
            "children": [["1.A.11.a"]],
        },
        "1.A.11.a.i": {
            "title": "Sorghum crop residues direct emissions",
            "comment": "Sorghum crop residues direct emissions",
            "info": {"gases": ["N2O"]},
        },
        "1.A.11.a.ii": {
            "title": "Sorghum crop residues indirect emissions",
            "comment": "Sorghum crop residues indirect emissions",
            "info": {"gases": ["N2O"]},
        },
        "1.A.11.a": {
            "title": "Sorghum crop residues",
            "comment": "Sorghum crop residues",
            "info": {"gases": ["N2O"]},
            "children": [["1.A.11.a.i", "1.A.11.a.ii"]],
        },
        "1.A.12": {
            "title": "Soya beans",
            "comment": "Soya beans",
            "info": {"gases": "N2O"},
            "children": [["1.A.12.a"]],
        },
        "1.A.12.a.i": {
            "title": "Soya beans crop residues direct emissions",
            "comment": "Soya beans crop residues direct emissions",
            "info": {"gases": ["N2O"]},
        },
        "1.A.12.a.ii": {
            "title": "Soya beans crop residues indirect emissions",
            "comment": "Soya beans crop residues indirect emissions",
            "info": {"gases": ["N2O"]},
        },
        "1.A.12.a": {
            "title": "Soya beans crop residues",
            "comment": "Soya beans crop residues",
            "info": {"gases": ["N2O"]},
            "children": [["1.A.12.a.i", "1.A.12.a.ii"]],
        },
        "1.B": {
            "title": "Synthetic fertilisers",
            "comment": "Synthetic fertilisers",
            "info": {"gases": ["N2O"]},
            "children": [["1.B.1", "1.B.2"]],
        },
        "1.B.1": {
            "title": "Direct emissions",
            "comment": "Direct emissions",
            "info": {"gases": ["N2O"]},
        },
        "1.B.2": {
            "title": "Indirect emissions",
            "comment": "Indirect emissions",
            "info": {"gases": ["N2O"]},
            "children": [["1.B.2.a", "1.B.2.b"]],
        },
        "1.B.2.a": {
            "title": "Indirect emissions that volatilise",
            "comment": "Indirect emissions that volatilise",
            "info": {"gases": ["N2O"]},
        },
        "1.B.2.b": {
            "title": "Indirect emissions that leach",
            "comment": "Indirect emissions that leach",
            "info": {"gases": ["N2O"]},
        },
        "2.A": {
            "title": "Natural gas",
            "comment": "Natural gas",
            "info": {"gases": ["CH4", "N2O", "CO2"]},
        },
        "2.B": {
            "title": "Electricity",
            "comment": "Electricity",
            "info": {"gases": ["CH4", "N2O", "CO2"]},
        },
        "2.C": {
            "title": "Coal",
            "comment": "Coal",
            "info": {"gases": ["CH4", "N2O", "CO2"]},
        },
        "2.D": {
            "title": "Heat",
            "comment": "Heat",
            "info": {"gases": ["CH4", "N2O", "CO2"]},
        },
        "2.E": {
            "title": "Petroleum",
            "comment": "Petroleum",
            "info": {"gases": ["CH4", "N2O", "CO2"]},
        },
        "3.A": {
            "title": "Asses",
            "comment": "Asses",
            "info": {"gases": ["CH4", "N2O"]},
        },
        "3.B": {
            "title": "Camels",
            "comment": "Camels",
            "info": {"gases": ["CH4", "N2O"]},
        },
        "3.C": {
            "title": "Cattle, dairy",
            "comment": "Cattle, dairy",
            "info": {"gases": ["CH4", "N2O"]},
        },
        "3.D": {
            "title": "Cattle, non-dairy",
            "comment": "Cattle, non-dairy",
            "info": {"gases": ["CH4", "N2O"]},
        },
        "3.E": {
            "title": "Chickens, broilers",
            "comment": "Chickens, broilers",
            "info": {"gases": ["N2O"]},
        },
        "3.F": {
            "title": "Chickens, layers",
            "comment": "Chickens, layers",
            "info": {"gases": ["N2O"]},
        },
        "3.G": {
            "title": "Goats",
            "comment": "Goats",
            "info": {"gases": ["CH4", "N2O"]},
        },
        "3.H": {
            "title": "Horses",
            "comment": "Horses",
            "info": {"gases": ["CH4", "N2O"]},
        },
        "3.I": {
            "title": "Mules and hinnies",
            "comment": "Mules and hinnies",
            "info": {"gases": ["CH4", "N2O"]},
        },
        "3.J": {
            "title": "Sheep",
            "comment": "Sheep",
            "info": {"gases": ["CH4", "N2O"]},
        },
        "3.K": {
            "title": "Llamas",
            "comment": "Llamas",
            "info": {"gases": ["CH4", "N2O"]},
        },
        "3.L": {"title": "Chickens", "comment": "Chickens", "info": {"gases": ["N2O"]}},
        "3.M": {
            "title": "Poultry Birds",
            "comment": "Poultry Birds",
            "info": {"gases": ["N2O"]},
        },
        "3.N": {
            "title": "Buffalo",
            "comment": "Buffalo",
            "info": {"gases": ["CH4", "N2O"]},
        },
        "3.O": {"title": "Ducks", "comment": "Ducks", "info": {"gases": ["N2O"]}},
        "3.P": {
            "title": "Swine, breeding",
            "comment": "Swine, breeding",
            "info": {"gases": ["CH4", "N2O"]},
        },
        "3.Q": {
            "title": "Swine, market",
            "comment": "Swine, market",
            "info": {"gases": ["CH4", "N2O"]},
        },
        "3.R": {"title": "Turkeys", "comment": "Turkeys", "info": {"gases": ["N2O"]}},
        "4": {
            "title": "Carbon stock change in forests",
            "comment": "Carbon stock change in forests",
            "info": {"gases": "CO2"},
            "children": [["4.A", "4.B"]],
        },
        "4.A": {
            "title": "Forest land",
            "comment": "Forest land",
            "info": {"gases": "CO2"},
        },
        "4.B": {
            "title": "Net Forest conversion",
            "comment": "Net Forest conversion",
            "info": {"gases": "CO2"},
        },
        "5": {
            "title": "Drained organic soils",
            "comment": "Drained organic soils",
            "info": {"gases": "CO2"},
            "children": [["5.A", "5.B"]],
        },
        "5.A": {
            "title": "Drained grassland",
            "comment": "Drained grassland",
            "info": {"gases": ["CO2", "N2O"]},
        },
        "5.B": {
            "title": "Drained cropland",
            "comment": "Drained cropland",
            "info": {"gases": ["CO2", "N2O"]},
        },
        "6.A.1": {
            "title": "Humid tropical forests",
            "comment": "Humid tropical forests",
            "info": {"gases": ["CO2", "N2O", "CH4"]},
        },
        "6.A.2": {
            "title": "Other forests",
            "comment": "Other forests",
            "info": {"gases": ["CO2", "N2O", "CH4"]},
        },
        "6.A": {
            "title": "Forest fires",
            "comment": "Forest fires",
            "info": {"gases": ["CO2", "N2O", "CH4"]},
            "children": [["6.A.1", "6.A.2"]],
        },
        "6.B.1": {
            "title": "Closed shrubland",
            "comment": "Closed shrubland",
            "info": {"gases": ["CO2", "N2O", "CH4"]},
        },
        "6.B.2": {
            "title": "Grassland",
            "comment": "Grassland",
            "info": {"gases": ["CO2", "N2O", "CH4"]},
        },
        "6.B.3": {
            "title": "Open shrubland",
            "comment": "Open shrubland",
            "info": {"gases": ["CO2", "N2O", "CH4"]},
        },
        "6.B.4": {
            "title": "Savanna",
            "comment": "Savanna",
            "info": {"gases": ["CO2", "N2O", "CH4"]},
        },
        "6.B.5": {
            "title": "Woody savanna",
            "comment": "Woody savanna",
            "info": {"gases": ["CO2", "N2O", "CH4"]},
        },
        "6.B": {
            "title": "Savanna fires",
            "comment": "Savanna fires",
            "info": {"gases": ["CO2", "N2O", "CH4"]},
            "children": [["6.B.1", "6.B.2", "6.B.3", "6.B.4", "6.B.5"]],
        },
        "6.C": {
            "title": "Fires in organic soils",
            "comment": "Fires in organic soils",
            "info": {"gases": ["CO2", "N2O", "CH4"]},
        },
        "6": {
            "title": "Fires",
            "comment": "Fires",
            "info": {"gases": ["CO2", "N2O", "CH4"]},
            "children": [["6.A", "6.B", "6.C"]],
        },
        "7.A": {
            "title": "Fertilizers Manufacturing",
            "comment": "Fertilizers Manufacturing",
            "info": {"gases": ["CO2", "N2O", "KYOTOGHG (AR5GWP100)"]},
        },
        "7.B": {
            "title": "Food Transport",
            "comment": "Food Transport",
            "info": {
                "gases": [
                    "CO2",
                    "CH4",
                    "N2O",
                    "KYOTOGHG (AR5GWP100)",
                    "FGASES (AR5GWP100)",
                ]
            },
        },
        "7.C": {
            "title": "Food Retail",
            "comment": "Food Retail",
            "info": {
                "gases": [
                    "CO2",
                    "CH4",
                    "N2O",
                    "KYOTOGHG (AR5GWP100)",
                    "FGASES (AR5GWP100)",
                ]
            },
        },
        "7.D": {
            "title": "Food Household Consumption",
            "comment": "Food Household Consumption",
            "info": {
                "gases": [
                    "CO2",
                    "CH4",
                    "N2O",
                    "KYOTOGHG (AR5GWP100)",
                    "FGASES (AR5GWP100)",
                ]
            },
        },
        "7.E": {
            "title": "Solid Food Waste",
            "comment": "Solid Food Waste",
            "info": {"gases": ["KYOTOGHG (AR5GWP100)", "CH4"]},
        },
        "7.F": {
            "title": "Domestic Wastewater",
            "comment": "Domestic Wastewater",
            "info": {"gases": ["KYOTOGHG (AR5GWP100)", "CH4", "N2O"]},
        },
        "7.G": {
            "title": "Industrial Wastewater",
            "comment": "Industrial Wastewater",
            "info": {"gases": ["KYOTOGHG (AR5GWP100)", "CH4", "N2O"]},
        },
        "7.H": {
            "title": "Incineration",
            "comment": "Incineration",
            "info": {"gases": ["CO2", "KYOTOGHG (AR5GWP100)"]},
        },
        "7.I": {
            "title": "Pre- and Post- Production",
            "comment": "Pre- and Post- Production",
            "info": {
                "gases": [
                    "CO2",
                    "CH4",
                    "N2O",
                    "KYOTOGHG (AR5GWP100)",
                    "FGASES (AR5GWP100)",
                ]
            },
        },
        "7.K": {
            "title": "Energy Use (Pre- and Post-Production)",
            "comment": "Energy Use (Pre- and Post-Production)",
            "info": {"gases": ["CO2", "CH4", "N2O", "KYOTOGHG (AR5GWP100)"]},
        },
        "7.L": {
            "title": "Agrifood Systems Waste Disposal",
            "comment": "Agrifood Systems Waste Disposal",
            "info": {"gases": ["CO2", "CH4", "N2O", "KYOTOGHG (AR5GWP100)"]},
        },
        "7.M": {
            "title": "Cold Chain F-Gas",
            "comment": "Cold Chain F-Gas",
            "info": {"gases": ["FGASES (AR5GWP100)"]},
        },
        "7": {
            "title": "Pre and post agricultural production",
            "comment": "Pre and post agricultural production",
            "info": {
                "gases": [
                    "CO2",
                    "CH4",
                    "N2O",
                    "KYOTOGHG (AR5GWP100)",
                    "FGASES (AR5GWP100)",
                ]
            },
            "children": [
                [
                    "7.A",
                    "7.B",
                    "7.C",
                    "7.D",
                    "7.E",
                    "7.F",
                    "7.G",
                    "7.H",
                    "7.I",
                    "7.K",
                    "7.L",
                    "7.M",
                ]
            ],
        },
    },
}
