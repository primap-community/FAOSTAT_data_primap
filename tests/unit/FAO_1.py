spec = {
    "name": "FAO",
    "title": "Food and Agriculture Organization of the United Nations (FAO) FAOSTAT data set categorisation",
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
            "children": [["1", "2"]],
        },
        "1": {
            "title": "Crops",
            "comment": "Crops",
            "children": [["1.A", "1.B"]],
            "info": {"gases": ["CH4", "N2O"]},
        },
        "2": {
            "title": "Energy use in agriculture",
            "comment": "Energy use in agriculture",
            "children": [["2.A", "2.B", "2.C", "2.D", "2.E"]],
            "info": {"gases": ["CH4", "N2O", "CO2"]},
        },
        "1.A": {
            "title": "All crops",
            "comment": "All crops",
            "children": [
                [
                    "1.A.1",
                    "1.A.2",
                    "1.A.3",
                    "1.A.4",
                    "1.A.5",
                    "1.A.6",
                    "1.A.7",
                    "1.A.8",
                    "1.A.9",
                    "1.A.10",
                    "1.A.11",
                    "1.A.12",
                ]
            ],
            "info": {"gases": ["CH4", "N2O"]},
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
            "children": [["1.A.1.a.ii", "1.A.1.a.i"]],
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
            "children": [["1.A.2.a.ii", "1.A.2.a.i"]],
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
            "children": [["1.A.3.a.ii", "1.A.3.a.i"]],
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
            "children": [["1.A.4.a.ii", "1.A.4.a.i"]],
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
            "children": [["1.A.5.a.ii", "1.A.5.a.i"]],
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
            "children": [["1.A.6.a.ii", "1.A.6.a.i"]],
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
            "children": [["1.A.7.a.ii", "1.A.7.a.i"]],
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
            "children": [["1.A.8.a.ii", "1.A.8.a.i"]],
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
            "children": [["1.A.9.a.ii", "1.A.9.a.i"]],
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
            "children": [["1.A.10.a.ii", "1.A.10.a.i"]],
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
            "children": [["1.A.11.a.ii", "1.A.11.a.i"]],
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
            "children": [["1.A.12.a.ii", "1.A.12.a.i"]],
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
    },
}
