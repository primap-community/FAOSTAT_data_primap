# Do not edit this file. It was auto-generated from the
# corresponding YAML file.
spec = {
    "name": "FAO",
    "title": (
        "Food and Agriculture Organization of the United Nations (FAO) "
        "FAOSTAT data set categorisation"
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
            "children": [["1", "2", "3"]],
        },
        "1": {
            "title": "Farm gate",
            "comment": "Farm gate",
            "info": {"gases": ["CO2", "CH4", "N2O"]},
            "children": [["1.A", "1.B", "1.C"]],
        },
        "1.A": {
            "title": "Crops",
            "comment": "Crops",
            "alternative_codes": ["1A"],
            "info": {"gases": ["CH4", "N2O"]},
            "children": [["1.A.1", "1.A.2"]],
        },
        "1.A.1": {
            "title": "Crops (excluding synthetic fertilisers)",
            "comment": "Crops (excluding synthetic fertilisers)",
            "alternative_codes": ["1A1"],
            "info": {"gases": ["CH4", "N2O"]},
            "children": [
                [
                    "1.A.1.a",
                    "1.A.1.b",
                    "1.A.1.c",
                    "1.A.1.d",
                    "1.A.1.e",
                    "1.A.1.f",
                    "1.A.1.g",
                    "1.A.1.h",
                    "1.A.1.i",
                    "1.A.1.j",
                    "1.A.1.k",
                    "1.A.1.l",
                ]
            ],
        },
        "1.A.1.a": {
            "title": "Wheat",
            "comment": "Wheat",
            "alternative_codes": ["1A1a"],
            "info": {"gases": ["CH4", "N2O"]},
            "children": [["1.A.1.a.i", "1.A.1.a.ii"]],
        },
        "1.A.1.a.i": {
            "title": "Wheat crop residues",
            "comment": "Wheat crop residues",
            "alternative_codes": ["1A1ai"],
            "info": {"gases": ["CH4", "N2O"]},
            "children": [["1.A.1.a.i.1", "1.A.1.a.i.2"]],
        },
        "1.A.1.a.i.1": {
            "title": "Wheat crop residues direct emissions",
            "comment": "Wheat crop residues direct emissions",
            "alternative_codes": ["1A1ai"],
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.1.a.i.2": {
            "title": "Wheat crop residues indirect emissions",
            "comment": "Wheat crop residues indirect emissions",
            "alternative_codes": ["1A1ai"],
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.1.a.ii": {
            "title": "Wheat burning crop residues",
            "comment": "Wheat burning crop residues",
            "alternative_codes": ["1A1aii"],
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.1.b": {
            "title": "Rice",
            "comment": "Rice",
            "alternative_codes": ["1A1b"],
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.1.b.i": {
            "title": "Rice crop residues",
            "comment": "Rice crop residues",
            "alternative_codes": ["1A1bi"],
            "info": {"gases": ["CH4", "N2O"]},
            "children": [["1.A.1.b.i.1", "1.A.1.b.i.2"]],
        },
        "1.A.1.b.i.1": {
            "title": "Rice crop residues direct emissions",
            "comment": "Rice crop residues direct emissions",
            "alternative_codes": ["1A1bi1"],
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.1.b.i.2": {
            "title": "Rice crop residues indirect emissions",
            "comment": "Rice crop residues indirect emissions",
            "alternative_codes": ["1A1bi2"],
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.1.b.ii": {
            "alternative_codes": ["1A1bii"],
            "title": "Rice burning crop residues",
            "comment": "Rice burning crop residues",
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.1.b.iii": {
            "title": "Rice cultivation",
            "comment": "Rice cultivation",
            "alternative_codes": ["1A1biii"],
            "info": {"gases": ["CH4"]},
        },
        "1.A.1.c": {
            "title": "Potatoes",
            "comment": "Potatoes",
            "alternative_codes": ["1A1c"],
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.1.c.i": {
            "title": "Potatoes crop residues",
            "comment": "Potatoes crop residues",
            "alternative_codes": ["1A1ci"],
            "info": {"gases": ["CH4", "N2O"]},
            "children": [["1.A.1.c.i.1", "1.A.1.c.i.2"]],
        },
        "1.A.1.c.i.1": {
            "title": "Potatoes crop residues direct emissions",
            "comment": "Potatoes crop residues direct emissions",
            "alternative_codes": ["1A1ci1"],
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.1.c.i.2": {
            "title": "Potatoes crop residues indirect emissions",
            "comment": "Potatoes crop residues indirect emissions",
            "alternative_codes": ["1A1ci2"],
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.1.d": {
            "title": "Millet",
            "comment": "Millet",
            "alternative_codes": "1A1d",
            "children": ["1.A.1.d.i"],
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.1.d.i.1": {
            "title": "Millet crop residues direct emissions",
            "comment": "Millet crop residues direct emissions",
            "alternative_codes": ["1A1di1"],
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.1.d.i.2": {
            "title": "Millet crop residues indirect emissions",
            "comment": "Millet crop residues indirect emissions",
            "alternative_codes": ["1A1di1"],
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.1.d.i": {
            "title": "Millet crop residues",
            "comment": "Millet crop residues",
            "alternative_codes": ["1A1di"],
            "info": {"gases": ["CH4", "N2O"]},
            "children": [["1.A.1.d.i.1", "1.A.1.d.i.2"]],
        },
        "1.A.1.e": {
            "title": "Barley",
            "comment": "Barley",
            "alternative_codes": "1A1e",
            "children": ["1.A.1.e.i"],
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.1.e.i.1": {
            "title": "Barley crop residues direct emissions",
            "comment": "Barley crop residues direct emissions",
            "alternative_codes": ["1A1ei1"],
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.1.e.i.2": {
            "title": "Barley crop residues indirect emissions",
            "comment": "Barley crop residues indirect emissions",
            "alternative_codes": ["1A1ei1"],
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.1.e.i": {
            "title": "Barley crop residues",
            "comment": "Barley crop residues",
            "alternative_codes": ["1A1ei"],
            "info": {"gases": ["CH4", "N2O"]},
            "children": [["1.A.1.e.i.1", "1.A.1.e.i.2"]],
        },
        "1.A.1.f": {
            "title": "Maize (corn)",
            "comment": "Maize (corn)",
            "alternative_codes": "1A1f",
            "children": ["1.A.1.f.i"],
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.1.f.i.1": {
            "title": "Maize (corn) crop residues direct emissions",
            "comment": "Maize (corn) crop residues direct emissions",
            "alternative_codes": ["1A1fi1"],
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.1.f.i.2": {
            "title": "Maize (corn) crop residues indirect emissions",
            "comment": "Maize (corn) crop residues indirect emissions",
            "alternative_codes": ["1A1fi1"],
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.1.f.i": {
            "title": "Maize (corn) crop residues",
            "comment": "Maize (corn) crop residues",
            "alternative_codes": ["1A1fi"],
            "info": {"gases": ["CH4", "N2O"]},
            "children": [["1.A.1.f.i.1", "1.A.1.f.i.2"]],
        },
        "1.A.1.f.ii": {
            "title": "Maize (corn) burning crop residues",
            "comment": "Maize (corn) burning crop residues",
            "alternative_codes": ["1A1fii"],
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.1.g": {
            "title": "Sugar cane",
            "comment": "Sugar cane",
            "alternative_codes": "1A1g",
            "children": ["1.A.1.g.i"],
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.1.g.i.1": {
            "title": "Sugar cane crop residues direct emissions",
            "comment": "Sugar cane crop residues direct emissions",
            "alternative_codes": ["1A1gi1"],
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.1.g.i.2": {
            "title": "Sugar cane crop residues indirect emissions",
            "comment": "Sugar cane crop residues indirect emissions",
            "alternative_codes": ["1A1gi1"],
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.1.g.i": {
            "title": "Sugar cane crop residues",
            "comment": "Sugar cane crop residues",
            "alternative_codes": ["1A1gi"],
            "info": {"gases": ["CH4", "N2O"]},
            "children": [["1.A.1.g.i.1", "1.A.1.g.i.2"]],
        },
        "1.A.1.g.ii": {
            "title": "Sugar cane burning crop residues",
            "comment": "Sugar cane burning crop residues",
            "alternative_codes": ["1A1gii"],
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.1.h": {
            "title": "Beans, dry",
            "comment": "Beans, dry",
            "alternative_codes": "1A1h",
            "children": ["1.A.1.h.i"],
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.1.h.i.1": {
            "title": "Beans, dry crop residues direct emissions",
            "comment": "Beans, dry crop residues direct emissions",
            "alternative_codes": ["1A1hi1"],
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.1.h.i.2": {
            "title": "Beans, dry crop residues indirect emissions",
            "comment": "Beans, dry crop residues indirect emissions",
            "alternative_codes": ["1A1hi1"],
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.1.h.i": {
            "title": "Beans, dry crop residues",
            "comment": "Beans, dry crop residues",
            "alternative_codes": ["1A1hi"],
            "info": {"gases": ["CH4", "N2O"]},
            "children": [["1.A.1.h.i.1", "1.A.1.h.i.2"]],
        },
        "1.A.1.i": {
            "title": "Oats",
            "comment": "Oats",
            "alternative_codes": "1A1i",
            "children": ["1.A.1.i.i"],
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.1.i.i.1": {
            "title": "Oats crop residues direct emissions",
            "comment": "Oats crop residues direct emissions",
            "alternative_codes": ["1A1ii1"],
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.1.i.i.2": {
            "title": "Oats crop residues indirect emissions",
            "comment": "Oats crop residues indirect emissions",
            "alternative_codes": ["1A1ii1"],
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.1.i.i": {
            "title": "Oats crop residues",
            "comment": "Oats crop residues",
            "alternative_codes": ["1A1ii"],
            "info": {"gases": ["CH4", "N2O"]},
            "children": [["1.A.1.i.i.1", "1.A.1.i.i.2"]],
        },
        "1.A.1.j": {
            "title": "Rye",
            "comment": "Rye",
            "alternative_codes": "1A1j",
            "children": ["1.A.1.j.i"],
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.1.j.i.1": {
            "title": "Rye crop residues direct emissions",
            "comment": "Rye crop residues direct emissions",
            "alternative_codes": ["1A1ji1"],
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.1.j.i.2": {
            "title": "Rye crop residues indirect emissions",
            "comment": "Rye crop residues indirect emissions",
            "alternative_codes": ["1A1ji1"],
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.1.j.i": {
            "title": "Rye crop residues",
            "comment": "Rye crop residues",
            "alternative_codes": ["1A1ji"],
            "info": {"gases": ["CH4", "N2O"]},
            "children": [["1.A.1.j.i.1", "1.A.1.j.i.2"]],
        },
        "1.A.1.k": {
            "title": "Sorghum",
            "comment": "Sorghum",
            "alternative_codes": "1A1k",
            "children": ["1.A.1.k.i"],
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.1.k.i.1": {
            "title": "Sorghum crop residues direct emissions",
            "comment": "Sorghum crop residues direct emissions",
            "alternative_codes": ["1A1ki1"],
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.1.k.i.2": {
            "title": "Sorghum crop residues indirect emissions",
            "comment": "Sorghum crop residues indirect emissions",
            "alternative_codes": ["1A1ki1"],
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.1.k.i": {
            "title": "Sorghum crop residues",
            "comment": "Sorghum crop residues",
            "alternative_codes": ["1A1ki"],
            "info": {"gases": ["CH4", "N2O"]},
            "children": [["1.A.1.k.i.1", "1.A.1.k.i.2"]],
        },
        "1.A.1.l": {
            "title": "Soya beans",
            "comment": "Soya beans",
            "alternative_codes": "1A1l",
            "children": ["1.A.1.l.i"],
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.1.l.i.1": {
            "title": "Soya beans crop residues direct emissions",
            "comment": "Soya beans crop residues direct emissions",
            "alternative_codes": ["1A1li1"],
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.1.l.i.2": {
            "title": "Soya beans crop residues indirect emissions",
            "comment": "Soya beans crop residues indirect emissions",
            "alternative_codes": ["1A1li1"],
            "info": {"gases": ["CH4", "N2O"]},
        },
        "1.A.1.l.i": {
            "title": "Soya beans crop residues",
            "comment": "Soya beans crop residues",
            "alternative_codes": ["1A1li"],
            "info": {"gases": ["CH4", "N2O"]},
            "children": [["1.A.1.l.i.1", "1.A.1.l.i.2"]],
        },
        "1.A.2": {
            "title": "Synthetic fertilisers",
            "comment": "Synthetic fertilisers",
            "alternative_codes": ["1A2"],
            "info": {"gases": ["N2O"]},
        },
        "1.B": {
            "title": "Livestock",
            "comment": "Livestock",
            "alternative_codes": ["1B"],
            "info": {"gases": ["CO2", "CH4", "N2O"]},
        },
        "1.C": {
            "title": "Energy use in agriculture",
            "comment": "Energy use in agriculture",
            "alternative_codes": ["1C"],
            "info": {"gases": ["CO2", "CH4", "N2O"]},
        },
        "2": {
            "title": "Land use and change",
            "comment": "Land use and change",
            "info": {"gases": ["CO2", "CH4", "N2O"]},
        },
        "3": {
            "title": "Pre and post agricultural production",
            "comment": "Pre and post agricultural production",
            "info": {"gases": ["CO2", "CH4", "N2O"]},
        },
    },
}
