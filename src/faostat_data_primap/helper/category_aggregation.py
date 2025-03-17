"""
Definitions for category aggregation.
"""

# Checking consistency of category tree in FAO categorisation
# There are discrepancies of up to 100% due to rounding errors for small values,
# for example, 0.0001 (rounded from 0.00006) + 0.0004 (rounded from 0.00036)
# = 0.00042 which is then rounded to 0.0004, while the consistency check expects 0.0005
# There are even more extreme example, where we need a tolerance of 100%:
# Eswatini, 1976:
# 1.A.1.a Crop residues (emissions N2O) = 0.0001
# 1.A.1.a.i Crop residues (Indirect emissions N2O) = 0
# 1.A.1.a.ii Crop residues (Direct emissions N2O) = 0
# Our way to deal with it, was to set the tolerance to 1% and look at the
# countries / sectors that yielded an error. If only a few countries and years
# are affected, it is likely just a rounding error. If all years are affected
# there may be something wrong with the data
agg_info_fao = {
    "category (FAO)": {
        "1.A.1.a": {  # wheat
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
        "1.A.2.a": {  # 1.A.2 rice
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
        # Only some crop types are burned on the field
        # Rounding errors up to 100% (see explanation above)
        "M.1.BCR": {
            "tolerance": 1,
            "sources": [
                "1.A.1.b",  # wheat
                "1.A.2.b",  # rice
                "1.A.6.b",  # maize (corn)
                "1.A.7.b",  # sugar cane
            ],
            "sel": {"variable": ["N2O", "CH4"]},
        },
        "M.1.CR": {  # N2O emissions from crop residues
            "tolerance": 1,
            "sources": [
                "M.1.CR.direct",  # direct emissions from crop residues
                "M.1.CR.indirect",  # indirect emissions from crop residues
            ],
            "sel": {"variable": ["N2O"]},
        },
        "1.A": {
            # crops
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
            "sel": {"variable": ["N2O", "CH4"]},
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
        # Category 1 is not available on FAO, so that's not a check
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
                # "3.M", # poultry is an aggregate of other categories, I forgot to remove
                "3.N",
                "3.O",
                "3.P",
                "3.Q",
                "3.R",
            ],
            "sel": {"variable": ["CH4", "N2O"]},
        },
        # Testing for one animal type to make sure the category tree makes sense
        # TODO: We could do the same for each animal
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
        "M.3.MA": {
            "tolerance": 1,
            "sources": [
                "M.3.MA.direct",
                "M.3.MA.indirect",
            ],
            "sel": {"variable": ["N2O"]},
        },
        "M.3.MP": {
            "tolerance": 1,
            "sources": [
                "M.3.MP.direct",
                "M.3.MP.indirect",
            ],
            "sel": {"variable": ["N2O"]},
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
            # rounding errors
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

# aggregating each gas separately to make this easier to understand
# We can change it back to one dict, once it's all sorted out
agg_info_ipcc2006_primap_N2O = {
    "category (IPCC2006_PRIMAP)": {
        "M.3.C.1.AG": {  # AG-related emissions from Biomass Burning
            "sources": [
                "3.C.1.b",  # Biomass Burning In Croplands (FAO M.1.BCR All Crops - Burning crop residues)
                "3.C.1.c",  # Biomass Burning in Grasslands (FAO 6.B savanna fires)
            ],
            "sel": {"variable": ["N2O"]},
        },
        "3.C.1": {  # Emissions from Biomass Burning (the same as M.3.C.1.AG)
            "sources": ["M.3.C.1.AG"],
            "sel": {"variable": ["N2O"]},
        },
        "3.C.4": {  # Direct N2O Emissions from Managed Soils
            # We currently only have direct and indirect emissions combined in one category.
            # Therefore, we need to make a decision how to classify it. We decided to map it all to
            # direct emissions. In does not make a difference for the primap-hist sectors,
            # but TODO direct / indirect should be mapped individually
            "sources": [
                "M.3.C.4.CR",  # Direct emissions from crop residues (FAO M.1.CR.direct),
                "M.3.C.4.MP",  # Direct emissions from manure left on pasture (FAO M.3.MP.direct)
                "M.3.C.4.MA",  # Direct emissions from manure applied to soils (FAO M.3.MA.direct)
                "3.C.4.a",  # synthetic fertilisers direct (FAO 1.B.1)
                "M.3.C.4.DOS.CL",  # Drained cropland (FAO 5.A drained cropland)
                "M.3.C.4.DOS.GL",  # Drained grassland (FAO 5.B drained grassland)
            ],
            "sel": {"variable": ["N2O"]},
        },
        "3.C.5": {  # Indirect N2O Emissions from Managed Soils
            "sources": [
                "M.3.C.5.SF",  # synthetic fertilisers indirect - there is no IPCC sub-category for this
                "M.3.C.5.CR",  # Indirect emissions from crop residues (FAO M.1.CR.indirect)
                "M.3.C.5.MP",  # Indirect emissions from manure left on pasture (FAO M.3.MP.indirect)
                "M.3.C.5.MA",  # Indirect emissions from manure applied to soils (FAO M.3.MA.indirect)
            ],
            "sel": {"variable": ["N2O"]},
        },
        "M.3.C.AG": {
            "sources": [
                "M.3.C.1.AG",  # AG-related emissions from Biomass Burning, same as 3.C.1
                "3.C.4",  # Direct N2O Emissions from Managed Soils
                "3.C.5",  # Indirect N2O Emissions from Managed Soils
            ],
            "sel": {"variable": ["N2O"]},
        },
        "M.AG.ELV": {
            "sources": ["M.3.C.AG"],
            "sel": {
                "variable": ["N2O"]
            },  # "M.3.D.AG" would be part of this, but does not exist
        },
        "3.C": {
            "sources": ["M.3.C.AG"],
            "sel": {"variable": ["N2O"]},
        },
        "3.A": {
            "sources": [
                "3.A.2"
            ],  # Manure management (3.A.1 is enteric fermentation and CH4 only)
            "sel": {"variable": ["N2O"]},
        },
        "M.AG": {
            "sources": [
                "3.A",
                "M.AG.ELV",
            ],
            "sel": {"variable": ["N2O"]},
        },
        "M.LULUCF": {
            "sources": [
                "3.B.1",  # Carbon stock change in forests (FAO 4, or 4.A and 4.B)
                # Note that IPCC M.3.C.1.a biomass burning in forest goes to LULUCF and not to AG. According to the FAO
                # mapping document it is part of forest land.
                # M.3.C.1.a for CO2 is an exception, because it is already included in the carbon stock change (FAO 4)
                "M.3.C.1.a",  # Biomass Burning In Forests (FAO 6.A forest fires)
            ],
            "sel": {"variable": ["N2O"]},
        },
        "3": {
            "sources": ["M.AG", "M.LULUCF"],
            "sel": {"variable": ["N2O"]},
        },
    }
}

agg_info_ipcc2006_primap_CO2 = {
    "category (IPCC2006_PRIMAP)": {
        # CO2 is LULUCF only
        # To see which CO2 categories are mapped to LULUCF, go to the FAOSTAT data explorer
        # and select for item: IPCC aggregates -> LULUCF list, elements: Emissions (CO2), years: any, country: any
        # There will be four items for each country: Forestland, Net Forest Conversion, Fires in Organic Soils,
        # and Drained Organic Soils (CO2)
        # The selection for IPCC Agriculture will be empty, that means CO2 is all LULUCF
        "3.B.2": {
            "sources": [
                "M.3.B.2.FOS",  # crop land - fires in organic soils (6.C Fires in organic soils)
                "M.3.B.2.DOS",  # crop land - drained organic soils (FAO 5.B Drained cropland)
            ],
            "sel": {"variable": ["CO2"]},
        },
        "3.B.3": {
            "sources": [
                "M.3.B.3.DOS",  # grass land - drained organic soils (FAO 5.A Drained grassland)
            ],
            "sel": {"variable": ["CO2"]},
        },
        "M.LULUCF": {
            "sources": [
                # Note that IPCC 3.B.1 comes from FAO 4 Carbon stock change in forests,
                # which is the sum of forestland and net forest conversion.
                # Also note that the category M.3.C.1.a (or FAO 6.A) forest fires would theoretically go
                # into LULUCF. However, according to https://files-faostat.fao.org/production/GT/GT_en.pdf
                # "The estimates from Forest fires exclude CO2, since these are
                # already covered in the carbon stock changes calculations carried out in the FAOSTAT
                # Forests domain." -> meaning CO2 is computed but not added to the LULUCF totals
                "3.B.1",  # Carbon stock change in forests (FAO 4, or 4.A and 4.B)
                "3.B.2",  # crop land
                "3.B.3",  # grass land
            ],
            "sel": {"variable": ["CO2"]},
        },
        "3": {
            "sources": ["M.LULUCF"],
            "sel": {"variable": ["CO2"]},
        },
    }
}

agg_info_ipcc2006_primap_CH4 = {
    "category (IPCC2006_PRIMAP)": {
        "3.A": {  # Livestock
            "sources": [
                "3.A.1",  # enteric fermentation (FAO M.3.EF)
                "3.A.2",  # manure management (FAO M.3.MM)
            ],
            "sel": {"variable": ["CH4"]},
        },
        "3.C.1": {  # Emissions from Biomass Burning
            "sources": [
                "3.C.1.b",  # Biomass Burning In Croplands (FAO M.1.BCR))
                "3.C.1.c",  # Biomass Burning in Grasslands (FAO 6.B savanna fires)
            ],
            "sel": {"variable": ["CH4"]},
        },
        "M.3.C.1.AG": {  # AG-related emissions from Biomass Burning
            "sources": [
                "3.C.1",  # Emissions from Biomass Burning
            ],
            "sel": {"variable": ["CH4"]},
        },
        "M.3.C.AG": {
            "sources": [
                "M.3.C.1.AG",  # AG-related emissions from Biomass Burning
                "3.C.7",  # rice cultivation (FAO 1.A.2.c Rice cultivation)
            ],
            "sel": {"variable": ["CH4"]},
        },
        "3.C": {
            "sources": [
                "M.3.C.1.AG",
            ],
            "sel": {"variable": ["CH4"]},
        },
        "M.AG.ELV": {
            "sources": [
                "M.3.C.AG",
            ],
            "sel": {"variable": ["CH4"]},
        },
        "M.AG": {
            "sources": [
                "3.A",  # Livestock
                "M.AG.ELV",  # Agriculture excluding livestock
            ],
            "sel": {"variable": ["CH4"]},
        },
        "M.LULUCF": {
            "sources": [
                "M.3.C.1.a",  # Biomass Burning In Forests (FAO 6.A forest fires)
                "M.3.B.2.FOS",  # cropland - fires in organic soils (FAO 6.C fires in organic soils)
            ],
            "sel": {"variable": ["CH4"]},
        },
        "3": {
            "sources": ["M.AG", "M.LULUCF"],
            "sel": {"variable": ["CH4"]},
        },
    }
}
