import climate_categories as cc
import primap2 as pm2
import pytest

from src.faostat_data_primap.helper.paths import downloaded_data_path
from src.faostat_data_primap.read import read_data


def test_read(tmp_path):
    domains_and_releases_to_read = [
        # ("farm_gate_agriculture_energy", "2024-11-14"),
        # ("farm_gate_emissions_crops", "2024-11-14"),
        ("farm_gate_livestock", "2024-11-14"),
        # ("land_use_drained_organic_soils", "2024-11-14"),
        # ("land_use_fires", "2024-11-14"),
        # ("land_use_forests", "2024-11-14"),
        # ("pre_post_agricultural_production", "2024-11-14"),
    ]

    read_data(
        domains_and_releases_to_read=domains_and_releases_to_read,
        read_path=downloaded_data_path,
        save_path=tmp_path,
    )


def test_yaml_to_python():
    cat = cc.from_yaml("FAO.yaml")
    cat.to_python("FAO.py")


def test_python_to_yaml():
    from FAO import spec

    cat = cc.from_spec(spec)
    assert cat


def test_make_dict_comprehension_for_faster_typing():
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
    }

    categories = {}
    # 0. main categories
    categories["0"] = {
        "title": "Total",
        "comment": "All emissions and removals",
        "children": [["1", "2"]],  #  , "3", "4", "5", "6", "7"]],
    }
    children_1 = ["1.A", "1.B"]
    children_2 = ["2.A", "2.B", "2.C", "2.D", "2.E"]
    children_3 = [f"3.{i}" for i in "ABCDEFGHIJKLMNOPQR"]
    children_4 = ["4.A"]
    children_5 = ["5.A", "5.B"]
    children_6 = ["6.A", "6.B", "6.C"]
    children_7 = [f"3.{i}" for i in "ABCDEFGHIJKLM"]
    main_categories = (
        # category code, name and comment, gases, children
        ("1", "Crops", ["CH4", "N2O"], children_1),
        (
            "2",
            "Energy use in agriculture",
            ["CH4", "N2O", "CO2"],
            children_2,
        ),
        # ("3", "Livestock", ["CH4", "N2O"], children_3),
        # ("4", "Forest", ["CO2"], children_4),
        # (
        #     "5",
        #     "Drained organic soils",
        #     ["N2O", "CO2"],
        #     children_5,
        # ),
        # ("6", "Fires", ["CH4", "N2O", "CO2"], children_6),
        # (
        #     "7",
        #     "Pre and post agricultural production",
        #     ["CH4", "N2O", "CO2"],
        #     children_7,
        # ),
    )
    for code, name, gases, children in main_categories:
        categories[code] = {
            "title": name,
            "comment": name,
            "alternative_codes": code.replace(".", ""),
            "children": [children],
            "info": {"gases": gases},
        }

    # 1. crops
    # all crops category
    code_all_crops = "1.A"
    codes_crops = [f"1.A.{i}" for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]]
    categories[code_all_crops] = {
        "title": "All crops",
        "comment": "All crops",
        "alternative_codes": code_all_crops.replace(".", ""),
        "children": [codes_crops],
        "info": {"gases": ["CH4", "N2O"]},
    }

    crops = [
        "Wheat",
        "Rice",
        "Potatoes",
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

    crop_burnings = [
        True,
        True,
        False,
        False,
        False,
        True,
        True,
        False,
        False,
        False,
        False,
        False,
    ]
    rice_cultivations = [
        False,
        True,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
        False,
    ]

    for crop, code, crop_burning, rice_cultivation in zip(
        crops, codes_crops, crop_burnings, rice_cultivations
    ):
        # all crops have at least N2O emissions
        gases_main = "N2O"

        if crop_burning or rice_cultivation:
            gases_main = ["CH4", "N2O"]

        # all crops have at least crop residues as child
        children_main = [f"{code}.a"]

        if crop_burning:
            children_main.append(f"{code}.b")

        if rice_cultivation:
            children_main.append(f"{code}.c")

        categories[f"{code}"] = {
            "title": f"{crop}",
            "comment": f"{crop}",
            "alternative_codes": [f"{code}".replace(".", "")],
            "info": {"gases": gases_main},
            "children": [children_main],
        }

        # crop residues (every crop has it)
        categories[f"{code}.a.i"] = {
            "title": f"{crop} crop residues direct emissions",
            "comment": f"{crop} crop residues direct emissions",
            "alternative_codes": [f"{code}.a".replace(".", "")],
            "info": {"gases": ["N2O"]},
        }

        categories[f"{code}.a.ii"] = {
            "title": f"{crop} crop residues indirect emissions",
            "comment": f"{crop} crop residues indirect emissions",
            "alternative_codes": [f"{code}.a.i".replace(".", "")],
            "info": {"gases": ["N2O"]},
        }

        categories[f"{code}.a"] = {
            "title": f"{crop} crop residues",
            "comment": f"{crop} crop residues",
            "alternative_codes": [f"{code}.a".replace(".", "")],
            "info": {"gases": ["N2O"]},
            "children": [[f"{code}.a.ii", f"{code}.a.i"]],
        }

        if crop_burning:
            categories[f"{code}.b"] = {
                "title": f"{crop} burning crop residues",
                "comment": f"{crop} burning crop residues",
                "alternative_codes": [f"{code}.b".replace(".", "")],
                "info": {"gases": ["CH4", "N2O"]},
            }
        if rice_cultivation:
            categories[f"{code}.c"] = {
                "title": "Rice cultivation",
                "comment": "Rice cultivation",
                "alternative_codes": [f"{code}.c".replace(".", "")],
                "info": {"gases": ["CH4"]},
            }

    # synthetic fertilisers
    codes_synthetic_fertilisers = ["1.B", "1.B.1", "1.B.2", "1.B.2.a", "1.B.2.b"]
    names = [
        "Synthetic fertilisers",
        "Direct emissions",
        "Indirect emissions",
        "Indirect emissions that volatilise",
        "Indirect emissions that leach",
    ]
    children_cats = [["1.B.1", "1.B.2"], None, ["1.B.2.a", "1.B.2.b"], None, None]

    for code, name, child_cat in zip(codes_synthetic_fertilisers, names, children_cats):
        categories[code] = {
            "title": name,
            "comment": name,
            "alternative_codes": [code.replace(".", "")],
            "info": {"gases": ["N2O"]},
        }
        if child_cat:
            categories[code]["children"] = [child_cat]

    # 2. energy use
    names = [
        "Natural gas",
        "Electricity",
        "Coal",
        "Heat",
        "Petroleum",
    ]
    codes = children_2
    for name, code in zip(names, codes):
        categories[code] = {
            "title": name,
            "comment": name,
            "alternative_codes": code.replace(".", ""),
            "info": {"gases": ["CH4", "N2O", "CO2"]},
        }

    spec["categories"] = categories
    cat = cc.HierarchicalCategorization.from_spec(spec.copy())
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
