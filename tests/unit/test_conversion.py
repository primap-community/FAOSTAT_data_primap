import climate_categories as cc
import primap2 as pm2
import pytest


def test_yaml_to_python():
    cat = cc.from_yaml("FAO.yaml")
    cat.to_python("FAO.py")


def test_make_dict_comprehension_for_faster_typing():
    crops = [
        "Millet",
        "Barley",
        "Maize (corn)",
        "Sugar cane",
        "Beans, dry",
        "Oats",
        "Rye",
        "Sorghum",
        "Soya beans",
    ]
    letters = ["d", "e", "f", "g", "h", "i", "j", "k", "l"]
    dict_crops = {}
    for crop, letter in zip(crops, letters):
        main_code = f"1.A.1.{letter}"
        crop_residues_code = f"1.A.1.{letter}.i"
        crop_residues_indirect_code = f"1.A.1.{letter}.i.2"
        crop_residues_direct_code = f"1.A.1.{letter}.i.1"

        dict_crops[main_code] = {
            "title": crop,
            "comment": crop,
            "alternative_codes": main_code.replace(".", ""),
            "children": [crop_residues_code],
            "info": {"gases": ["CH4", "N2O"]},
        }

        dict_crops[crop_residues_direct_code] = {
            "title": f"{crop} crop residues direct emissions",
            "comment": f"{crop} crop residues direct emissions",
            "alternative_codes": [crop_residues_direct_code.replace(".", "")],
            "info": {"gases": ["CH4", "N2O"]},
        }

        dict_crops[crop_residues_indirect_code] = {
            "title": f"{crop} crop residues indirect emissions",
            "comment": f"{crop} crop residues indirect emissions",
            "alternative_codes": [crop_residues_direct_code.replace(".", "")],
            "info": {"gases": ["CH4", "N2O"]},
        }

        dict_crops[crop_residues_code] = {
            "title": f"{crop} crop residues",
            "comment": f"{crop} crop residues",
            "alternative_codes": [crop_residues_code.replace(".", "")],
            "info": {"gases": ["CH4", "N2O"]},
            "children": [[crop_residues_direct_code, crop_residues_indirect_code]],
        }
        # "1.A.1.c.i.1": {
        #     "title" : "Potatoes crop residues direct emissions",
        #     "comment" : "Potatoes crop residues direct emissions",
        #     "alternative_codes" : ["1A1ci1"],
        #     "info" : {"gases" : ["CH4", "N2O"]},
        # },
        # "1.A.1.c.i.2": {
        #     "title" : "Potatoes crop residues indirect emissions",
        #     "comment" : "Potatoes crop residues indirect emissions",
        #     "alternative_codes" : ["1A1ci2"],
        #     "info" : {"gases" : ["CH4", "N2O"]},
        # },
    pass


{
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
}


@pytest.mark.xfail
def test_conversion_from_FAO_to_IPCC2006_PRIMAP():
    # make categorisation A from yaml
    categorisation_a = cc.from_yaml("FAO.yaml")

    # make categorisation B from yaml
    categorisation_b = cc.IPCC2006_PRIMAP

    # categories not part of climate categories so we need to add them manually
    cats = {
        "A": categorisation_a,
        "B": categorisation_b,
    }

    # make conversion from csv
    conv = cc.Conversion.from_csv("conversion.FAO.IPPCC2006_PRIMAP.csv", cats=cats)

    ds = pm2.open_dataset(
        "extracted_data/v2024-11-14/FAOSTAT_Agrifood_system_emissions_v2024-11-14.nc"
    )

    result = ds.pr.convert(
        dim="category",
        conversion=conv,
        auxiliary_dimensions={"gas": "source (gas)"},
    )

    assert result
