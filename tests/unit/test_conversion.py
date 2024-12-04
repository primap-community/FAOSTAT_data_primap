import climate_categories as cc
import primap2 as pm2
import pytest


def test_yaml_to_python():
    cat = cc.from_yaml("FAO.yaml")
    cat.to_python("FAO.py")


def test_python_to_yaml():
    from FAO import spec

    cat = cc.from_spec(spec)
    assert cat


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
    pass


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
