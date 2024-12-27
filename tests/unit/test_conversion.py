import climate_categories as cc
import primap2 as pm2
import xarray as xr

from src.faostat_data_primap.helper.category_aggregation import (
    agg_info_fao,
    agg_info_ipcc2006_primap,
)
from src.faostat_data_primap.helper.paths import (
    downloaded_data_path,
    extracted_data_path,
)
from src.faostat_data_primap.read import read_data


def test_conversion_from_FAO_to_IPCC2006_PRIMAP():
    # make categorisation A from yaml
    categorisation_a = cc.from_python("FAO.py")
    # make categorisation B from yaml
    categorisation_b = cc.IPCC2006_PRIMAP

    # category FAOSTAT not yet part of climate categories, so we need to add it manually
    cats = {
        "FAOSTAT": categorisation_a,
        "IPCC2006_PRIMAP": categorisation_b,
    }

    ds_fao = (
        extracted_data_path
        / "v2024-11-14/FAOSTAT_Agrifood_system_emissions_v2024-11-14_raw.nc"
    )
    ds = pm2.open_dataset(ds_fao)
    # consistency check in original categorisation
    # drop UNFCCC data
    ds = ds.drop_sel(source="UNFCCC")
    #
    # # Checking consistency of category tree in FAO categorisation
    # # There are discrepancies of up to 100% due to rounding errors for small values
    # # theoretical example, 0.0001 (rounded from 0.00006) + 0.0004 (rounded from 0.00036)
    # # = 0.00042 which is then rounded to 0.0004, while the consistency check expects 0.0005
    # # At the moment, we are only checking categories that will later be used by primap-hist.
    # # If we want to use other categories we should expand this consistency check.
    # agg_info_fao = {
    #     "category (FAOSTAT)": {
    #         # 1.A.1 wheat
    #         # rounding errors
    #         "1.A.1.a": {
    #             "tolerance": 1,
    #             "sources": [
    #                 "1.A.1.a.i",
    #                 "1.A.1.a.ii",
    #             ],
    #             "sel": {"variable": ["N2O"]},
    #         },
    #         "1.A.1": {
    #             "tolerance": 0.01,
    #             "sources": [
    #                 "1.A.1.a",
    #                 "1.A.1.b",
    #             ],
    #             "sel": {"variable": ["N2O", "CH4"]},
    #         },
    #         # 1.A.2 rice
    #         # rounding errors
    #         "1.A.2.a": {
    #             "tolerance": 1,
    #             "sources": [
    #                 "1.A.2.a.i",
    #                 "1.A.2.a.ii",
    #             ],
    #             "sel": {"variable": ["N2O"]},
    #         },
    #         "1.A.2": {
    #             "tolerance": 0.01,
    #             "sources": [
    #                 "1.A.2.a",
    #                 "1.A.2.b",
    #                 "1.A.2.c",  # rice cultivation CH4
    #             ],
    #             "sel": {"variable": ["N2O", "CH4"]},
    #         },
    #         # potatoes
    #         "1.A.3.a": {
    #             "tolerance": 1,
    #             "sources": [
    #                 "1.A.3.a.i",
    #                 "1.A.3.a.ii",
    #             ],
    #             "sel": {"variable": ["N2O"]},
    #         },
    #         "1.A.3": {
    #             "tolerance": 0.01,
    #             "sources": [
    #                 "1.A.3.a",
    #             ],
    #             "sel": {"variable": ["N2O"]},
    #         },
    #         # millet
    #         "1.A.4.a": {
    #             "tolerance": 1,
    #             "sources": [
    #                 "1.A.4.a.i",
    #                 "1.A.4.a.ii",
    #             ],
    #             "sel": {"variable": ["N2O"]},
    #         },
    #         "1.A.4": {
    #             "tolerance": 0.01,
    #             "sources": [
    #                 "1.A.4.a",
    #             ],
    #             "sel": {"variable": ["N2O"]},
    #         },
    #         # barley
    #         "1.A.5.a": {
    #             "tolerance": 1,
    #             "sources": [
    #                 "1.A.5.a.i",
    #                 "1.A.5.a.ii",
    #             ],
    #             "sel": {"variable": ["N2O"]},
    #         },
    #         "1.A.5": {
    #             "tolerance": 0.01,
    #             "sources": [
    #                 "1.A.5.a",
    #             ],
    #             "sel": {"variable": ["N2O"]},
    #         },
    #         # barley
    #         "1.A.6.a": {
    #             "tolerance": 1,
    #             "sources": [
    #                 "1.A.6.a.i",
    #                 "1.A.6.a.ii",
    #             ],
    #             "sel": {"variable": ["N2O"]},
    #         },
    #         "1.A.6": {
    #             "tolerance": 0.01,
    #             "sources": [
    #                 "1.A.6.a",
    #                 "1.A.6.b",
    #             ],
    #             "sel": {"variable": ["N2O", "CH4"]},
    #         },
    #         # sugar cane
    #         "1.A.7.a": {
    #             "tolerance": 1,
    #             "sources": [
    #                 "1.A.7.a.i",
    #                 "1.A.7.a.ii",
    #             ],
    #             "sel": {"variable": ["N2O"]},
    #         },
    #         "1.A.7": {
    #             "tolerance": 0.01,
    #             "sources": [
    #                 "1.A.7.a",
    #                 "1.A.7.b",
    #             ],
    #             "sel": {"variable": ["N2O", "CH4"]},
    #         },
    #         # dry beans
    #         "1.A.8.a": {
    #             "tolerance": 1,
    #             "sources": [
    #                 "1.A.8.a.i",
    #                 "1.A.8.a.ii",
    #             ],
    #             "sel": {"variable": ["N2O"]},
    #         },
    #         "1.A.8": {
    #             "tolerance": 0.01,
    #             "sources": [
    #                 "1.A.8.a",
    #             ],
    #             "sel": {"variable": ["N2O"]},
    #         },
    #         # oats
    #         "1.A.9.a": {
    #             "tolerance": 1,
    #             "sources": [
    #                 "1.A.9.a.i",
    #                 "1.A.9.a.ii",
    #             ],
    #             "sel": {"variable": ["N2O"]},
    #         },
    #         "1.A.9": {
    #             "tolerance": 0.01,
    #             "sources": [
    #                 "1.A.9.a",
    #             ],
    #             "sel": {"variable": ["N2O"]},
    #         },
    #         # rye
    #         "1.A.10.a": {
    #             "tolerance": 1,
    #             "sources": [
    #                 "1.A.10.a.i",
    #                 "1.A.10.a.ii",
    #             ],
    #             "sel": {"variable": ["N2O"]},
    #         },
    #         "1.A.10": {
    #             "tolerance": 0.01,
    #             "sources": [
    #                 "1.A.10.a",
    #             ],
    #             "sel": {"variable": ["N2O"]},
    #         },
    #         # sorghum
    #         "1.A.11.a": {
    #             "tolerance": 1,
    #             "sources": [
    #                 "1.A.11.a.i",
    #                 "1.A.11.a.ii",
    #             ],
    #             "sel": {"variable": ["N2O"]},
    #         },
    #         "1.A.11": {
    #             "tolerance": 0.01,
    #             "sources": [
    #                 "1.A.11.a",
    #             ],
    #             "sel": {"variable": ["N2O"]},
    #         },
    #         # soya beans
    #         "1.A.12.a": {
    #             "tolerance": 1,
    #             "sources": [
    #                 "1.A.12.a.i",
    #                 "1.A.12.a.ii",
    #             ],
    #             "sel": {"variable": ["N2O"]},
    #         },
    #         "1.A.12": {
    #             "tolerance": 0.01,
    #             "sources": [
    #                 "1.A.12.a",
    #             ],
    #             "sel": {"variable": ["N2O"]},
    #         },
    #         "1.A": {
    #             # some rounding errors for CH4
    #             "tolerance": 1,
    #             "sources": [
    #                 "1.A.1",
    #                 "1.A.2",
    #                 "1.A.3",
    #                 "1.A.4",
    #                 "1.A.5",
    #                 "1.A.6",
    #                 "1.A.7",
    #                 "1.A.8",
    #                 "1.A.9",
    #                 "1.A.10",
    #                 "1.A.11",
    #                 "1.A.12",
    #             ],
    #         },
    #         "1.B.2": {
    #             "tolerance": 0.01,
    #             "sources": [
    #                 "1.B.2.a",
    #                 "1.B.2.b",
    #             ],
    #             "sel": {"variable": ["N2O"]},
    #         },
    #         "1.B": {
    #             "tolerance": 1,
    #             "sources": [
    #                 "1.B.1",
    #                 "1.B.2",
    #             ],
    #             "sel": {"variable": ["N2O"]},
    #         },
    #         # Category 1 is not available on FAOSTAT, so that's not a check
    #         "1": {
    #             "tolerance": 0.01,
    #             "sources": [
    #                 "1.A",
    #                 "1.B",
    #             ],
    #         },
    #         "3": {
    #             # mostly rounding errors, Macedonia slightly higher than 100% discrepancy
    #             # Saint Pierre and Miquelon, 1992, N20 200% error, considered negligible
    #             "tolerance": 2.01,
    #             "sources": [
    #                 "3.A",
    #                 "3.B",
    #                 "3.C",
    #                 "3.D",
    #                 "3.E",
    #                 "3.F",
    #                 "3.G",
    #                 "3.H",
    #                 "3.I",
    #                 "3.J",
    #                 "3.K",
    #                 "3.L",
    #                 # "3.M", # poultry is an aggregate of other categories I forgot to remove
    #                 "3.N",
    #                 "3.O",
    #                 "3.P",
    #                 "3.Q",
    #                 "3.R",
    #             ],
    #             "sel": {"variable": ["CH4", "N2O"]},
    #         },
    #         # Testing for one animal type to make sure the category tree makes sense
    #         # TODO: We could do the same for each animal but that's a lot of effort
    #         "3.C.3.b" : {
    #             "tolerance": 1,
    #             "sources": [
    #                 "3.C.3.b.i",
    #                 "3.C.3.b.ii",
    #             ],
    #             "sel": {"variable": ["N2O"]},
    #         },
    #         "3.C.3" : {
    #             "tolerance" : 1,
    #             "sources" : [
    #                 "3.C.3.a",
    #                 "3.C.3.b",
    #             ],
    #             "sel" : {"variable" : ["N2O"]},
    #         },
    #         "3.C.2.b" : {
    #             "tolerance" : 1,
    #             "sources" : [
    #                 "3.C.2.b.i",
    #                 "3.C.2.b.ii",
    #             ],
    #             "sel" : {"variable" : ["N2O"]},
    #         },
    #         "3.C.2" : {
    #             "tolerance" : 1,
    #             "sources" : [
    #                 "3.C.2.a",
    #                 "3.C.2.b",
    #             ],
    #             "sel" : {"variable" : ["N2O"]},
    #         },
    #         "3.C.1" : {
    #             "tolerance" : 1,
    #             "sources" : [
    #                 "3.C.1.a",
    #                 "3.C.1.b",
    #                 "3.C.1.c",
    #             ],
    #             "sel" : {"variable" : ["N2O", "CH4"]},
    #         },
    #         "3.C" : {
    #             "tolerance" : 1,
    #             "sources" : [
    #                 "3.C.1",
    #                 "3.C.2",
    #                 "3.C.3",
    #                 "3.C.4",
    #             ],
    #             "sel" : {"variable" : ["N2O", "CH4"]},
    #         },
    #         "4": {
    #             "tolerance": 0.01,
    #             "sources": [
    #                 "4.A",
    #                 "4.B",
    #             ],
    #             "sel": {"variable": ["CO2"]},
    #         },
    #         "5" : {
    #             "tolerance" : 0.2,
    #             "sources" : [
    #                 "5.A",
    #                 "5.B",
    #             ],
    #             "sel" : {"variable" : ["CO2", "N2O"]},
    #         },
    #         "6.A" : {
    #             "tolerance" : 1,
    #             "sources" : [
    #                 "6.A.1",
    #                 "6.A.2",
    #             ],
    #             "sel" : {"variable" : ["CH4", "N2O", "CO2"]},
    #         },
    #         "6.B": {
    #             # rounding errors, NLD looks problematic but hard to tell which value is right
    #             "tolerance": 1,
    #             "sources": [
    #                 "6.B.1",
    #                 "6.B.2",
    #                 "6.B.3",
    #                 "6.B.4",
    #                 "6.B.5",
    #             ],
    #             "sel": {"variable": ["CH4", "N2O", "CO2"]},
    #         },
    #         "6" : {
    #             "tolerance" : 0.01,
    #             "sources" : [
    #                 "6.A",
    #                 "6.B",
    #                 "6.C",
    #             ],
    #             "sel" : {"variable" : ["CH4", "N2O", "CO2"]},
    #         },
    #     }
    # }
    ds_checked = ds.pr.add_aggregates_coordinates(agg_info=agg_info_fao)  # noqa: F841

    # ds_checked_if = ds_checked.pr.to_interchange_format()
    # We need a comversion CSV file for each entity
    # That's a temporary workaround until convert function can filter for data variables (entities)
    conv = {}
    gases = ["CO2", "CH4", "N2O"]
    for var in gases:
        conv[var] = cc.Conversion.from_csv(
            f"../../conversion_FAO_IPPCC2006_PRIMAP_{var}.csv", cats=cats
        )

    # convert for each entity
    da_dict = {}
    for var in gases:
        da_dict[var] = ds[var].pr.convert(
            dim="category (FAOSTAT)",
            conversion=conv[var],
        )
    result = xr.Dataset(da_dict)
    result.attrs = ds.attrs
    result.attrs["cat"] = "category (IPCC2006_PRIMAP)"

    # convert to interchange format and back to get rid of empty categories
    result_if = result.pr.to_interchange_format()
    result = pm2.pm2io.from_interchange_format(result_if)

    # agg_info_ipcc2006_primap = {
    #     "category (IPCC2006_PRIMAP)": {
    #         "3.C.1": {
    #             "sources": ["3.C.1.a", "3.C.1.b", "3.C.1.c"],
    #         },
    #         "M.3.C.AG": {
    #             "sources": [
    #                 "3.C.1.b",  # Biomass Burning In Croplands
    #                 "3.C.1.c",  # Biomass Burning in Grasslands
    #                 "3.C.4",  # Direct N2O Emissions from Managed Soils
    #                 "3.C.5",  # Indirect N2O Emissions from Managed Soils
    #                 "3.C.6",  # Indirect N2O Emissions from Manure Management
    #             ],
    #         },
    #         "M.AG.ELV": {
    #             "sources": ["M.3.C.AG"],  # "M.3.D.AG" is zero
    #         },
    #         "3.C": {
    #             "sources": [
    #                 "3.C.1",
    #                 "3.C.2",
    #                 "3.C.3",
    #                 "3.C.4",
    #                 "3.C.5",
    #                 "3.C.6",
    #                 "3.C.7",
    #             ]
    #         },
    #         # "3.D" : {"sources" : ["3.D.1", "3.D.2"]}, # we don't have it
    #         "3.A.1.a": {  # cattle (dairy) + cattle (non-dairy)
    #             "sources": [
    #                 "3.A.1.a.i",
    #                 "3.A.1.a.ii",
    #             ]
    #         },
    #         "3.A.1": {
    #             "sources": [
    #                 "3.A.1.a",
    #                 "3.A.1.b",
    #                 "3.A.1.c",
    #                 "3.A.1.d",
    #                 "3.A.1.e",
    #                 "3.A.1.f",
    #                 "3.A.1.g",
    #                 "3.A.1.h",  # 3.A.1.i poultry left out because it is a group of categories
    #                 "3.A.1.j",
    #             ]
    #         },
    #         "3.A.2.a": {  # decomposition of manure cattle (dairy) + cattle (non-dairy)
    #             "sources": [
    #                 "3.A.2.a.i",
    #                 "3.A.2.a.ii",
    #             ]
    #         },
    #         "3.A.2": {
    #             "sources": [
    #                 "3.A.2.a",
    #                 "3.A.2.b",
    #                 "3.A.2.c",
    #                 "3.A.2.d",
    #                 "3.A.2.e",
    #                 "3.A.2.f",
    #                 "3.A.2.g",
    #                 "3.A.2.h",
    #                 "3.A.2.i",
    #                 "3.A.2.j",
    #             ]
    #         },
    #         "3.A": {"sources": ["3.A.1", "3.A.2"]},
    #         "M.AG": {"sources": ["3.A", "M.AG.ELV"]},
    #         # "M.3.D.LU": {"sources": ["3.D.1"]},
    #         # For LULUCF Forest Land, Cropland, Grassland, is all we have
    #         "M.LULUCF": {
    #             "sources": [
    #                 "3.B.1",  # Carbon stock change in forests
    #                 "3.B.2",  # Drained grassland
    #                 "3.B.3",  # Drained cropland
    #                 "3.C.1.a",  # Biomass Burning In Forests
    #             ]
    #         },  # forest fires
    #         "3": {"sources": ["M.AG", "M.LULUCF"]},
    #     }
    # }

    result_proc = result.pr.add_aggregates_coordinates(
        agg_info=agg_info_ipcc2006_primap
    )

    result_proc_if = result_proc.pr.to_interchange_format()

    # save processed data
    release_name = "v2024-11-14"
    output_filename = f"FAOSTAT_Agrifood_system_emissions_{release_name}"
    output_folder = extracted_data_path / release_name

    if not output_folder.exists():
        output_folder.mkdir()

    filepath = output_folder / (output_filename + ".csv")
    print(f"Writing processed primap2 file to {filepath}")
    pm2.pm2io.write_interchange_format(
        filepath,
        result_proc_if,
    )

    compression = dict(zlib=True, complevel=9)
    encoding = {var: compression for var in result_proc.data_vars}
    filepath = output_folder / (output_filename + ".nc")
    print(f"Writing netcdf file to {filepath}")
    result_proc.pr.to_netcdf(filepath, encoding=encoding)


def test_read(tmp_path):
    domains_and_releases_to_read = [
        # ("farm_gate_agriculture_energy", "2024-11-14"),
        # ("farm_gate_emissions_crops", "2024-11-14"),
        # ("farm_gate_livestock", "2024-11-14"),
        # ("land_use_drained_organic_soils", "2024-11-14"),
        ("land_use_fires", "2023-11-09"),
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


def test_make_dict_comprehension_for_faster_typing():  # noqa: PLR0912 PLR0915
    spec = {
        "name": "FAOSTAT",
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
        "children": [["1", "2", "3", "4", "5", "6", "7"]],
    }
    children_1 = ["1.A", "1.B"]
    children_2 = ["2.A", "2.B", "2.C", "2.D", "2.E"]
    children_3 = [f"3.{i}" for i in "ABCDEFGHIJKLMNOPQR"]
    # children_4 = ["4.A"]
    # children_5 = ["5.A", "5.B"]
    # children_6 = ["6.A", "6.B", "6.C"]
    # children_7 = [f"3.{i}" for i in "ABCDEFGHIJKLM"]
    main_categories = (
        # category code, name and comment, gases, children
        ("1", "Crops", ["CH4", "N2O"], children_1),
        (
            "2",
            "Energy use in agriculture",
            ["CH4", "N2O", "CO2"],
            children_2,
        ),
        ("3", "Livestock", ["CH4", "N2O"], children_3),
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
            # "alternative_codes": code.replace(".", ""),
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
        # "alternative_codes": code_all_crops.replace(".", ""),
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
            # "alternative_codes": [f"{code}".replace(".", "")],
            "info": {"gases": gases_main},
            "children": [children_main],
        }

        # crop residues (every crop has it)
        categories[f"{code}.a.i"] = {
            "title": f"{crop} crop residues direct emissions",
            "comment": f"{crop} crop residues direct emissions",
            # "alternative_codes": [f"{code}.a".replace(".", "")],
            "info": {"gases": ["N2O"]},
        }

        categories[f"{code}.a.ii"] = {
            "title": f"{crop} crop residues indirect emissions",
            "comment": f"{crop} crop residues indirect emissions",
            # "alternative_codes": [f"{code}.a.i".replace(".", "")],
            "info": {"gases": ["N2O"]},
        }

        categories[f"{code}.a"] = {
            "title": f"{crop} crop residues",
            "comment": f"{crop} crop residues",
            # "alternative_codes": [f"{code}.a".replace(".", "")],
            "info": {"gases": ["N2O"]},
            "children": [[f"{code}.a.ii", f"{code}.a.i"]],
        }

        if crop_burning:
            categories[f"{code}.b"] = {
                "title": f"{crop} burning crop residues",
                "comment": f"{crop} burning crop residues",
                # "alternative_codes": [f"{code}.b".replace(".", "")],
                "info": {"gases": ["CH4", "N2O"]},
            }
        if rice_cultivation:
            categories[f"{code}.c"] = {
                "title": "Rice cultivation",
                "comment": "Rice cultivation",
                # "alternative_codes": [f"{code}.c".replace(".", "")],
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
            # "alternative_codes": [code.replace(".", "")],
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
            # "alternative_codes": code.replace(".", ""),
            "info": {"gases": ["CH4", "N2O", "CO2"]},
        }

    # 3 livestock
    animals = [
        "Asses",
        "Camels",
        "Cattle, dairy",
        "Cattle, non-dairy",
        "Chickens, broilers",
        "Chickens, layers",
        "Goats",
        "Horses",
        "Mules and hinnies",
        "Sheep",
        "Llamas",
        "Chickens",
        "Poultry Birds",
        "Buffalo",
        "Ducks",
        "Swine, breeding",
        "Swine, market",
        "Turkeys",
    ]

    codes_animals = [f"3.{i}" for i in "ABCDEFGHIJKLMNOPQR"]

    enteric_fermentation = [
        "Asses",
        "Camels",
        "Cattle, dairy",
        "Cattle, non-dairy",
        "Goats",
        "Horses",
        "Sheep",
        "Mules and hinnies",
        "Buffalo",
        "Swine, breeding",
        "Swine, market",
        "Llamas",
    ]

    for animal, code in zip(animals, codes_animals):
        if animal in enteric_fermentation:
            gases = ["CH4"]
            animal_children = [f"{code}.{i}" for i in "1234"]
            categories[f"{code}.4"] = {
                "title": f"{animal} enteric fermentation",
                "comment": f"{animal} enteric fermentation",
                # "alternative_codes" : code.replace(".", ""),
                "info": {"gases": gases},
            }
        else:
            gases = ["N2O"]
            animal_children = [f"{code}.{i}" for i in "123"]

        categories[code] = {
            "title": animal,
            "comment": animal,
            # "alternative_codes" : code.replace(".", ""),
            "info": {"gases": gases},
            "children": [animal_children],
        }

        # manure management branch
        manure_management_children = [f"{code}.1.{i}" for i in "abc"]
        categories[f"{code}.1"] = {
            "title": f"{animal} manure management",
            "comment": f"{animal} manure management",
            # "alternative_codes" : code.replace(".", ""),
            "info": {"gases": gases},
            "children": [manure_management_children],
        }

        categories[f"{code}.1.a"] = {
            "title": f"{animal} decomposition of organic matter",
            "comment": f"{animal} decomposition of organic matter",
            # "alternative_codes" : code.replace(".", ""),
            "info": {"gases": "CH4"},
        }

        categories[f"{code}.1.b"] = {
            "title": f"{animal} manure management (Direct emissions N2O)",
            "comment": f"{animal} manure management (Direct emissions N2O)",
            # "alternative_codes" : code.replace(".", ""),
            "info": {"gases": "N2O"},
        }

        categories[f"{code}.1.c"] = {
            "title": f"{animal} manure management (Indirect emissions N2O)",
            "comment": f"{animal} manure management (Indirect emissions N2O)",
            # "alternative_codes" : code.replace(".", ""),
            "info": {"gases": "N2O"},
        }

        # manure left on pasture branch
        manure_left_on_pasture_children = [f"{code}.2.{i}" for i in "ab"]
        categories[f"{code}.2"] = {
            "title": f"{animal} manure left on pasture",
            "comment": f"{animal} manure left on pasture",
            # "alternative_codes" : code.replace(".", ""),
            "info": {"gases": "N2O"},
            "children": [manure_left_on_pasture_children],
        }

        categories[f"{code}.2.a"] = {
            "title": f"{animal} manure left on pasture (direct emissions N2O)",
            "comment": f"{animal} manure left on pasture (direct emissions N2O)",
            # "alternative_codes" : code.replace(".", ""),
            "info": {"gases": "N2O"},
        }

        categories[f"{code}.2.b"] = {
            "title": f"{animal} manure left on pasture (indirect emissions N2O)",
            "comment": f"{animal} manure left on pasture (indirect emissions N2O)",
            # "alternative_codes" : code.replace(".", ""),
            "info": {"gases": "N2O"},
            "children": [[f"{code}.2.b.i", f"{code}.2.b.ii"]],
        }

        categories[f"{code}.2.b.i"] = {
            "title": (
                f"{animal} manure left on pasture "
                f"(indirect emissions, N2O that leaches)"
            ),
            "comment": (
                f"{animal} manure left on pasture (indirect "
                f"emissions, N2O that leaches)"
            ),
            # "alternative_codes" : code.replace(".", ""),
            "info": {"gases": "N2O"},
        }

        categories[f"{code}.2.b.ii"] = {
            "title": (
                f"{animal} manure left on pasture "
                f"(indirect emissions, N2O that volatilises)"
            ),
            "comment": (
                f"{animal} manure left on pasture (indirect "
                f"emissions, N2O that volatilises)"
            ),
            # "alternative_codes" : code.replace(".", ""),
            "info": {"gases": "N2O"},
        }

        # manure applied branch

        manure_applied_children = [f"{code}.3.{i}" for i in "ab"]
        categories[f"{code}.3"] = {
            "title": f"{animal} manure applied",
            "comment": f"{animal} manure applied",
            # "alternative_codes" : code.replace(".", ""),
            "info": {"gases": "N2O"},
            "children": [manure_applied_children],
        }

        categories[f"{code}.3.a"] = {
            "title": f"{animal} manure applied (direct emissions N2O)",
            "comment": f"{animal} manure applied (direct emissions N2O)",
            # "alternative_codes" : code.replace(".", ""),
            "info": {"gases": "N2O"},
        }

        categories[f"{code}.3.b"] = {
            "title": f"{animal} manure applied (indirect emissions N2O)",
            "comment": f"{animal} manure applied (indirect emissions N2O)",
            # "alternative_codes" : code.replace(".", ""),
            "info": {"gases": "N2O"},
            "children": [[f"{code}.3.b.i", f"{code}.3.b.ii"]],
        }

        categories[f"{code}.3.b.i"] = {
            "title": (
                f"{animal} manure applied " f"(indirect emissions, N2O that leaches)"
            ),
            "comment": (
                f"{animal} manure applied (indirect " f"emissions, N2O that leaches)"
            ),
            # "alternative_codes" : code.replace(".", ""),
            "info": {"gases": "N2O"},
        }

        categories[f"{code}.3.b.ii"] = {
            "title": (
                f"{animal} manure applied "
                f"(indirect emissions, N2O that volatilises)"
            ),
            "comment": (
                f"{animal} manure applied (indirect "
                f"emissions, N2O that volatilises)"
            ),
            # "alternative_codes" : code.replace(".", ""),
            "info": {"gases": "N2O"},
        }

    # forests
    categories["4"] = {
        "title": "Carbon stock change in forests",
        "comment": "Carbon stock change in forests",
        "info": {"gases": "CO2"},
        "children": [["4.A", "4.B"]],
    }

    categories["4.A"] = {
        "title": "Forest land",
        "comment": "Forest land",
        "info": {"gases": "CO2"},
    }

    categories["4.B"] = {
        "title": "Net Forest conversion",
        "comment": "Net Forest conversion",
        "info": {"gases": "CO2"},
    }

    # drained organic soils
    categories["5"] = {
        "title": "Drained organic soils",
        "comment": "Drained organic soils",
        "info": {"gases": "CO2"},
        "children": [["5.A", "5.B"]],
    }

    categories["5.A"] = {
        "title": "Drained grassland",
        "comment": "Drained grassland",
        "info": {"gases": ["CO2", "N2O"]},
    }

    categories["5.B"] = {
        "title": "Drained cropland",
        "comment": "Drained cropland",
        "info": {"gases": ["CO2", "N2O"]},
    }

    # 6 Fires
    # Forest fires
    forest_fires_children = ["Humid tropical forests", "Other forests"]
    forest_fires_children_codes = ["6.A.1", "6.A.2"]
    for cat_name, code in zip(forest_fires_children, forest_fires_children_codes):
        categories[code] = {
            "title": cat_name,
            "comment": cat_name,
            "info": {"gases": ["CO2", "N2O", "CH4"]},
        }
    categories["6.A"] = {
        "title": "Forest fires",
        "comment": "Forest fires",
        "info": {"gases": ["CO2", "N2O", "CH4"]},
        "children": [forest_fires_children_codes],
    }

    # Savanna fires
    savanna_fires_children = [
        "Closed shrubland",
        "Grassland",
        "Open shrubland",
        "Savanna",
        "Woody savanna",
    ]
    savanna_fires_children_codes = ["6.B.1", "6.B.2", "6.B.3", "6.B.4", "6.B.5"]
    for cat_name, code in zip(savanna_fires_children, savanna_fires_children_codes):
        categories[code] = {
            "title": cat_name,
            "comment": cat_name,
            "info": {"gases": ["CO2", "N2O", "CH4"]},
        }
    categories["6.B"] = {
        "title": "Savanna fires",
        "comment": "Savanna fires",
        "info": {"gases": ["CO2", "N2O", "CH4"]},
        "children": [savanna_fires_children_codes],
    }

    # fires in organic soils
    categories["6.C"] = {
        "title": "Fires in organic soils",
        "comment": "Fires in organic soils",
        "info": {"gases": ["CO2", "N2O", "CH4"]},
    }

    # 6 fires
    categories["6"] = {
        "title": "Fires",
        "comment": "Fires",
        "info": {"gases": ["CO2", "N2O", "CH4"]},
        "children": [["6.A", "6.B", "6.C"]],
    }

    # 7 pre and post production
    pre_post_production_categories = [
        "Fertilizers Manufacturing",
        "Food Transport",
        "Food Retail",
        "Food Household Consumption",
        "Solid Food Waste",
        "Domestic Wastewater",
        "Industrial Wastewater",
        "Incineration",
        "Pre- and Post- Production",
        "Energy Use (Pre- and Post-Production)",
        "Agrifood Systems Waste Disposal",
        "Cold Chain F-Gas",
        "Pesticides Manufacturing",
        "Food Processing",
        "Food Packaging",
    ]
    pre_post_production_categories_codes = ["7." + i for i in "ABCDEFGHIJKLMNO"]
    pre_post_production_categories_gases = [
        ["CO2", "N2O", "KYOTOGHG (AR5GWP100)"],
        ["CO2", "CH4", "N2O", "KYOTOGHG (AR5GWP100)", "FGASES (AR5GWP100)"],
        ["CO2", "CH4", "N2O", "KYOTOGHG (AR5GWP100)", "FGASES (AR5GWP100)"],
        ["CO2", "CH4", "N2O", "KYOTOGHG (AR5GWP100)", "FGASES (AR5GWP100)"],
        ["KYOTOGHG (AR5GWP100)", "CH4"],
        ["KYOTOGHG (AR5GWP100)", "CH4", "N2O"],
        ["KYOTOGHG (AR5GWP100)", "CH4", "N2O"],
        ["CO2", "KYOTOGHG (AR5GWP100)"],  # incineration
        ["CO2", "CH4", "N2O", "KYOTOGHG (AR5GWP100)", "FGASES (AR5GWP100)"],
        ["CO2", "CH4", "N2O", "KYOTOGHG (AR5GWP100)"],
        ["CO2", "CH4", "N2O", "KYOTOGHG (AR5GWP100)"],
        ["FGASES (AR5GWP100)"],
        ["CO2", "CH4", "N2O", "KYOTOGHG (AR5GWP100)"],
        ["CO2", "CH4", "N2O", "KYOTOGHG (AR5GWP100)", "FGASES (AR5GWP100)"],
        ["CO2", "CH4", "N2O", "KYOTOGHG (AR5GWP100)"],
    ]
    for cat_name, code, gases in zip(
        pre_post_production_categories,
        pre_post_production_categories_codes,
        pre_post_production_categories_gases,
    ):
        categories[code] = {
            "title": cat_name,
            "comment": cat_name,
            "info": {"gases": gases},
        }
    categories["7"] = {
        "title": "Pre and post agricultural production",
        "comment": "Pre and post agricultural production",
        "info": {
            "gases": [
                "CO2",
                "CH4",
                "N2O",
                "KYOTOGHG (AR5GWP100)",
                "FGASES (AR5GWP100)",
            ],
        },
        "children": [pre_post_production_categories_codes],
    }

    spec["categories"] = categories
    fao_cats = cc.HierarchicalCategorization.from_spec(spec.copy())
    # run print(fao_cats.show_as_tree())
    fao_cats.to_python("FAO.py")
    fao_cats.to_yaml("FAO.yaml")
    pass
