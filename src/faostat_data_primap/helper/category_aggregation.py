"""
Definitions for category aggregation.
"""

# Checking consistency of category tree in FAO categorisation
# There are discrepancies of up to 100% due to rounding errors for small values
# theoretical example, 0.0001 (rounded from 0.00006) + 0.0004 (rounded from 0.00036)
# = 0.00042 which is then rounded to 0.0004, while the consistency check expects 0.0005
# At the moment, we are only checking categories that will later be used by primap-hist.
# If we want to use other categories we should expand this consistency check.
agg_info_fao = {
    "category (FAO)": {
        # 1.A.1 wheat
        # rounding errors
        "1.A.1.a": {
            "tolerance": 1,
            "sources": [
                "1.A.1.a.i",
                "1.A.1.a.ii",
            ],
            "sel": {"variable": ["N2O"]},
        },
        "1.A.1": {
            "tolerance": 1,
            "sources": [
                "1.A.1.a",
                "1.A.1.b",
            ],
            "sel": {"variable": ["N2O", "CH4"]},
        },
        # 1.A.2 rice
        # rounding errors
        "1.A.2.a": {
            "tolerance": 1,
            "sources": [
                "1.A.2.a.i",
                "1.A.2.a.ii",
            ],
            "sel": {"variable": ["N2O"]},
        },
        "1.A.2": {
            "tolerance": 1,
            "sources": [
                "1.A.2.a",
                "1.A.2.b",
                "1.A.2.c",  # rice cultivation CH4
            ],
            "sel": {"variable": ["N2O", "CH4"]},
        },
        # potatoes
        "1.A.3.a": {
            "tolerance": 1,
            "sources": [
                "1.A.3.a.i",
                "1.A.3.a.ii",
            ],
            "sel": {"variable": ["N2O"]},
        },
        "1.A.3": {
            "tolerance": 1,
            "sources": [
                "1.A.3.a",
            ],
            "sel": {"variable": ["N2O"]},
        },
        # millet
        "1.A.4.a": {
            "tolerance": 1,
            "sources": [
                "1.A.4.a.i",
                "1.A.4.a.ii",
            ],
            "sel": {"variable": ["N2O"]},
        },
        "1.A.4": {
            "tolerance": 1,
            "sources": [
                "1.A.4.a",
            ],
            "sel": {"variable": ["N2O"]},
        },
        # barley
        "1.A.5.a": {
            "tolerance": 1,
            "sources": [
                "1.A.5.a.i",
                "1.A.5.a.ii",
            ],
            "sel": {"variable": ["N2O"]},
        },
        "1.A.5": {
            "tolerance": 0.01,
            "sources": [
                "1.A.5.a",
            ],
            "sel": {"variable": ["N2O"]},
        },
        # barley
        "1.A.6.a": {
            "tolerance": 1,
            "sources": [
                "1.A.6.a.i",
                "1.A.6.a.ii",
            ],
            "sel": {"variable": ["N2O"]},
        },
        "1.A.6": {
            "tolerance": 1,
            "sources": [
                "1.A.6.a",
                "1.A.6.b",
            ],
            "sel": {"variable": ["N2O", "CH4"]},
        },
        # sugar cane
        "1.A.7.a": {
            "tolerance": 1,
            "sources": [
                "1.A.7.a.i",
                "1.A.7.a.ii",
            ],
            "sel": {"variable": ["N2O"]},
        },
        "1.A.7": {
            "tolerance": 1,
            "sources": [
                "1.A.7.a",
                "1.A.7.b",
            ],
            "sel": {"variable": ["N2O", "CH4"]},
        },
        # dry beans
        "1.A.8.a": {
            "tolerance": 1,
            "sources": [
                "1.A.8.a.i",
                "1.A.8.a.ii",
            ],
            "sel": {"variable": ["N2O"]},
        },
        "1.A.8": {
            "tolerance": 1,
            "sources": [
                "1.A.8.a",
            ],
            "sel": {"variable": ["N2O"]},
        },
        # oats
        "1.A.9.a": {
            "tolerance": 1,
            "sources": [
                "1.A.9.a.i",
                "1.A.9.a.ii",
            ],
            "sel": {"variable": ["N2O"]},
        },
        "1.A.9": {
            "tolerance": 1,
            "sources": [
                "1.A.9.a",
            ],
            "sel": {"variable": ["N2O"]},
        },
        # rye
        "1.A.10.a": {
            "tolerance": 1,
            "sources": [
                "1.A.10.a.i",
                "1.A.10.a.ii",
            ],
            "sel": {"variable": ["N2O"]},
        },
        "1.A.10": {
            "tolerance": 1,
            "sources": [
                "1.A.10.a",
            ],
            "sel": {"variable": ["N2O"]},
        },
        # sorghum
        "1.A.11.a": {
            "tolerance": 1,
            "sources": [
                "1.A.11.a.i",
                "1.A.11.a.ii",
            ],
            "sel": {"variable": ["N2O"]},
        },
        "1.A.11": {
            "tolerance": 1,
            "sources": [
                "1.A.11.a",
            ],
            "sel": {"variable": ["N2O"]},
        },
        # soya beans
        "1.A.12.a": {
            "tolerance": 1,
            "sources": [
                "1.A.12.a.i",
                "1.A.12.a.ii",
            ],
            "sel": {"variable": ["N2O"]},
        },
        "1.A.12": {
            "tolerance": 1,
            "sources": [
                "1.A.12.a",
            ],
            "sel": {"variable": ["N2O"]},
        },
        "1.A": {
            # some rounding errors for CH4
            "tolerance": 1,
            "sources": [
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
            ],
        },
        "1.B.2": {
            "tolerance": 1,
            "sources": [
                "1.B.2.a",
                "1.B.2.b",
            ],
            "sel": {"variable": ["N2O"]},
        },
        "1.B": {
            "tolerance": 1,
            "sources": [
                "1.B.1",
                "1.B.2",
            ],
            "sel": {"variable": ["N2O"]},
        },
        # Category 1 is not available on FAOS, so that's not a check
        "1": {
            "tolerance": 0.01,
            "sources": [
                "1.A",
                "1.B",
            ],
        },
        "3": {
            # mostly rounding errors, Macedonia slightly higher than 100% discrepancy
            # Saint Pierre and Miquelon, 1992, N20 200% error, considered negligible
            "tolerance": 2.01,
            "sources": [
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
                # "3.M", # poultry is an aggregate of other categories I forgot to remove
                "3.N",
                "3.O",
                "3.P",
                "3.Q",
                "3.R",
            ],
            "sel": {"variable": ["CH4", "N2O"]},
        },
        # Testing for one animal type to make sure the category tree makes sense
        # TODO: We could do the same for each animal but that's a lot of effort
        "3.C.3.b": {
            "tolerance": 1,
            "sources": [
                "3.C.3.b.i",
                "3.C.3.b.ii",
            ],
            "sel": {"variable": ["N2O"]},
        },
        "3.C.3": {
            "tolerance": 1,
            "sources": [
                "3.C.3.a",
                "3.C.3.b",
            ],
            "sel": {"variable": ["N2O"]},
        },
        "3.C.2.b": {
            "tolerance": 1,
            "sources": [
                "3.C.2.b.i",
                "3.C.2.b.ii",
            ],
            "sel": {"variable": ["N2O"]},
        },
        "3.C.2": {
            "tolerance": 1,
            "sources": [
                "3.C.2.a",
                "3.C.2.b",
            ],
            "sel": {"variable": ["N2O"]},
        },
        "3.C.1": {
            "tolerance": 1,
            "sources": [
                "3.C.1.a",
                "3.C.1.b",
                "3.C.1.c",
            ],
            "sel": {"variable": ["N2O", "CH4"]},
        },
        "3.C": {
            "tolerance": 1,
            "sources": [
                "3.C.1",
                "3.C.2",
                "3.C.3",
                "3.C.4",
            ],
            "sel": {"variable": ["N2O", "CH4"]},
        },
        "4": {
            "tolerance": 0.01,
            "sources": [
                "4.A",
                "4.B",
            ],
            "sel": {"variable": ["CO2"]},
        },
        "5": {
            "tolerance": 0.2,
            "sources": [
                "5.A",
                "5.B",
            ],
            "sel": {"variable": ["CO2", "N2O"]},
        },
        "6.A": {
            "tolerance": 1,
            "sources": [
                "6.A.1",
                "6.A.2",
            ],
            "sel": {"variable": ["CH4", "N2O", "CO2"]},
        },
        "6.B": {
            # rounding errors, NLD looks problematic but hard to tell which value is right
            "tolerance": 1,
            "sources": [
                "6.B.1",
                "6.B.2",
                "6.B.3",
                "6.B.4",
                "6.B.5",
            ],
            "sel": {"variable": ["CH4", "N2O", "CO2"]},
        },
        "6": {
            "tolerance": 0.01,
            "sources": [
                "6.A",
                "6.B",
                "6.C",
            ],
            "sel": {"variable": ["CH4", "N2O", "CO2"]},
        },
    }
}

agg_info_ipcc2006_primap = {
    "category (IPCC2006_PRIMAP)": {
        "3.C.1": {  # Emissions from Biomass Burning
            "sources": [
                "3.C.1.a",  # Biomass Burning In Forest Lands
                "3.C.1.b",  # Biomass Burning In Croplands
                "3.C.1.c",  # Biomass Burning in Grasslands
            ],
        },
        "M.3.C.AG": {
            "sources": [
                "3.C.1.b",  # Biomass Burning In Croplands - looks good (CH4, N2O)
                "3.C.1.c",  # Biomass Burning in Grasslands - looks good (CH4)
                "3.C.4",  # Direct N2O Emissions from Managed Soils
                "M.3.C.4.SF",  # synthetic fertilisers
                "3.C.5",  # Indirect N2O Emissions from Managed Soils
                "M.3.C.5.SF",  # synthetic fertilisers
                "3.C.6",  # Indirect N2O Emissions from Manure Management
                "3.C.7",  # rice cultivation
            ],
        },
        "M.AG.ELV": {
            "sources": ["M.3.C.AG"],  # "M.3.D.AG" is zero
        },
        "3.C": {
            "sources": [
                "3.C.1",
                "3.C.2",
                "3.C.3",
                "3.C.4",  # excluding synthetic fertilisers
                "M.3.C.4.SF",  # synthetic fertilisers
                "3.C.5",  # excluding synthetic fertilisers
                "M.3.C.5.SF",  # synthetic fertilisers
                "3.C.6",
                "3.C.7",
            ]
        },
        "3.A.1.a": {  # enteric fermentation
            "sources": [
                "3.A.1.a.i",  # cattle (dairy)
                "3.A.1.a.ii",  # cattle (non-dairy)
            ]
        },
        "3.A.1": {  # enteric fermentation
            "sources": [
                "3.A.1.a",
                "3.A.1.b",
                "3.A.1.c",
                "3.A.1.d",
                "3.A.1.e",
                "3.A.1.f",
                "3.A.1.g",
                "3.A.1.h",
                "3.A.1.j",
            ]
        },
        "3.A.2.a": {  # decomposition of manure - CH4, N2O
            "sources": [
                "3.A.2.a.i",  # cattle (dairy)
                "3.A.2.a.ii",  # cattle (non-dairy)
            ]
        },
        "3.A.2": {  # decomposition of manure - CH4, N2O
            "sources": [
                "3.A.2.a",
                "3.A.2.b",
                "3.A.2.c",
                "3.A.2.d",
                "3.A.2.e",
                "3.A.2.f",
                "3.A.2.g",
                "3.A.2.h",
                "3.A.2.i",
                "3.A.2.j",
            ]
        },
        "3.A": {"sources": ["3.A.1", "3.A.2"]},
        "M.AG": {"sources": ["3.A", "M.AG.ELV"]},
        "M.LULUCF": {
            "sources": [
                "3.B.1",  # Carbon stock change in forests
                "3.B.2",  # Drained grassland
                "3.B.3",  # Drained cropland
                "3.C.1.a",  # Biomass Burning In Forests
            ]
        },
        "3": {"sources": ["M.AG", "M.LULUCF"]},
    }
}
