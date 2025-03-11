"""read data set"""

import os
import pathlib

import climate_categories as cc
import pandas as pd
import primap2 as pm2  # type: ignore
import xarray
import xarray as xr

from faostat_data_primap.helper.category_aggregation import (
    agg_info_fao,
    agg_info_ipcc2006_primap_CH4,
    agg_info_ipcc2006_primap_CO2,
    agg_info_ipcc2006_primap_N2O,
)
from faostat_data_primap.helper.country_mapping import country_to_iso3_mapping
from faostat_data_primap.helper.definitions import (
    config_to_if,
    read_config_all,
)
from faostat_data_primap.helper.paths import (
    downloaded_data_path,
    extracted_data_path,
    root_path,
)


def get_all_domains(downloaded_data_path: pathlib.Path) -> list[str]:
    """
    Get a list of all available domains.

    Parameters
    ----------
    downloaded_data_path
        The path to the downloaded data sets.

    Returns
    -------
        All domains in the downloaded data directory.

    """
    return [
        domain
        for domain in os.listdir(downloaded_data_path)
        if (downloaded_data_path / domain).is_dir()
    ]


def get_latest_release(domain_path: pathlib.Path) -> str:
    """
    Get the latest release in a domain directory.

    Parameters
    ----------
    domain_path
        The path to the domain

    Returns
    -------
    Name of the directory with latest data.

    """
    all_releases = [
        release_name
        for release_name in os.listdir(domain_path)
        if (domain_path / release_name).is_dir()
    ]
    return sorted(all_releases, reverse=True)[0]


# TODO split out functions to avoid PLR0915
def read_data(  # noqa: PLR0915 PLR0912
    read_path: pathlib.Path,
    domains_and_releases_to_read: list[tuple[str, str]],
    save_path: pathlib.Path,
) -> None:
    """
    Read specified domains and releases and save output files.

    Parameters
    ----------
    read_path
        Where to look for the downloaded data
    domains_and_releases_to_read
        The domains and releases to use
    save_path
        The path to save the data to

    """
    df_list = []
    for domain, release in domains_and_releases_to_read:
        read_config = read_config_all[domain][release]

        print(f"Read {read_config['filename']}")
        dataset_path = read_path / domain / release / read_config["filename"]

        # There are some non-utf8 characters
        df_domain = pd.read_csv(dataset_path, encoding="ISO-8859-1")

        if "items_to_remove" in read_config.keys():
            df_domain = df_domain[
                ~df_domain["Item"].isin(read_config["items_to_remove"])
            ]

        # remove rows by element
        if "elements_to_remove" in read_config.keys():
            df_domain = df_domain[
                ~df_domain["Element"].isin(read_config["elements_to_remove"])
            ]

        # remove rows by area
        if "areas_to_remove" in read_config.keys():
            df_domain = df_domain[
                ~df_domain["Area"].isin(read_config["areas_to_remove"])
            ]

        # create country columns
        df_domain["country (ISO3)"] = df_domain["Area"].map(country_to_iso3_mapping)

        # check all countries are converted into iso3 codes
        if any(df_domain["country (ISO3)"].isna()):
            msg = f"Not all countries are converted into ISO3 codes for {domain}"
            raise ValueError(msg)

        # create entity column
        df_domain["entity"] = df_domain["Element"].map(read_config["entity_mapping"])

        # check all entities are mapped
        if any(df_domain["entity"].isna()):
            msg = f"Not all entities are mapped for {domain}"
            raise ValueError(msg)

        # create category column (combination of Item and Element works best)
        df_domain["Item - Element"] = df_domain["Item"] + " - " + df_domain["Element"]

        if "category_mapping_item_element" in read_config.keys():
            df_domain["category"] = df_domain["Item - Element"].map(
                read_config["category_mapping_item_element"]
            )

        # sometimes there are too many categories per domain to write
        # everything in the config file
        # TODO we could do this for crops as well, but it's not necessary
        if ("category_mapping_element" in read_config.keys()) and (
            "category_mapping_item" in read_config.keys()
        ):
            # split steps for easier debugging
            df_domain["mapped_item"] = df_domain["Item"].map(
                read_config["category_mapping_item"]
            )
            df_domain["mapped_element"] = df_domain["Element"].map(
                read_config["category_mapping_element"]
            )
            if "category" in df_domain.columns:
                df_domain["category_1"] = (
                    df_domain["mapped_item"] + df_domain["mapped_element"]
                )
                df_domain["category"] = df_domain["category"].fillna(
                    df_domain["category_1"]
                )
                df_domain = df_domain.drop(
                    labels=["category_1"],
                    axis=1,
                )
            else:
                df_domain["category"] = (
                    df_domain["mapped_item"] + df_domain["mapped_element"]
                )
            df_domain = df_domain.drop(
                labels=[
                    "mapped_item",
                    "mapped_element",
                ],
                axis=1,
            )

        # some rows can only be removed by Item - Element column
        if "items-elements_to_remove" in read_config.keys():
            df_domain = df_domain[
                ~df_domain["Item - Element"].isin(
                    read_config["items-elements_to_remove"]
                )
            ]
        # else:
        #     msg = f"Could not find mapping for {domain=}."
        #     raise ValueError(msg)

        # drop combined item - element columns
        df_domain = df_domain.drop(
            labels=[
                "Item - Element",
            ],
            axis=1,
        )

        # check if all Item-Element combinations are now converted to category codes
        fao_categories = list(cc.FAO.df.index)
        unknown_categories = [
            i for i in df_domain.category.unique() if i not in fao_categories
        ]
        if unknown_categories:
            msg = (
                f"Not all categories are part of FAO categorisation. "
                f"Check mapping for {unknown_categories} in domain {domain}"
            )
            raise ValueError(msg)

        # drop columns we don't need
        df_domain = df_domain.drop(
            read_config["columns_to_drop"],
            axis=1,
        )

        df_list.append(df_domain)

    df_all = pd.concat(df_list, axis=0, join="outer", ignore_index=True)

    # some domains don't have Source column or values are empty
    # we assume these values come from FAO
    # TODO Better not to hard-code this in case the label changes
    if "Source" not in df_all.columns:
        df_all["Source"] = "FAO TIER 1"
    else:
        df_all["Source"] = df_all["Source"].fillna("FAO TIER 1")

    # Remove the "Y" prefix for the years columns
    df_all = df_all.rename(columns=lambda x: x.lstrip("Y") if x.startswith("Y") else x)

    # Make sure the units are correct
    df_all["Unit"] = df_all["entity"] + " * " + df_all["Unit"] + "/ year"
    df_all["Unit"] = df_all["Unit"].replace(read_config_all["replace_units"])

    date_last_updated = sorted(
        [i[1] for i in domains_and_releases_to_read], reverse=True
    )[0]
    release_name = f"v{date_last_updated}"

    data_if = pm2.pm2io.convert_wide_dataframe_if(
        df_all,
        coords_cols=config_to_if["coords_cols"],
        coords_defaults={
            "scenario": release_name,
        },
        coords_terminologies=config_to_if["coords_terminologies"],
        coords_value_mapping=config_to_if["coords_value_mapping"],
        filter_keep=config_to_if["filter_keep"],
        filter_remove=config_to_if["filter_remove"],
        meta_data=config_to_if["meta_data"],
    )

    # convert to PRIMAP2 native format
    data_pm2 = pm2.pm2io.from_interchange_format(data_if, data_if.attrs)

    # convert back to IF for standardized units
    data_if = data_pm2.pr.to_interchange_format()

    # save raw data
    output_filename = f"FAOSTAT_Agrifood_system_emissions_{release_name}_raw"

    if not save_path.exists():
        save_path.mkdir()

    output_folder = save_path / release_name
    if not output_folder.exists():
        output_folder.mkdir()

    filepath = output_folder / (output_filename + ".csv")
    print(f"Writing raw primap2 file to {filepath}")
    pm2.pm2io.write_interchange_format(
        filepath,
        data_if,
    )

    compression = dict(zlib=True, complevel=9)
    encoding = {var: compression for var in data_pm2.data_vars}
    filepath = output_folder / (output_filename + ".nc")
    print(f"Writing netcdf file to {filepath}")
    data_pm2.pr.to_netcdf(filepath, encoding=encoding)

    # process data - conversion and category aggregation
    # todo variable naming
    result_proc = process(data_pm2)

    # save processed data
    result_proc_if = result_proc.pr.to_interchange_format()

    output_filename = f"FAOSTAT_Agrifood_system_emissions_{release_name}"
    # output_folder = extracted_data_path / release_name

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


def process(ds: xarray.Dataset) -> xarray.Dataset:
    """
    Process dataset.

    Perform the conversion from FAO to IPCC2006_PRIMAP categories
    and aggregate categories.

    Parameters
    ----------
    ds
        The data set to process.

    Returns
    -------
        The processed dataset

    """
    # make categorisation A from yaml
    categorisation_a = cc.FAO
    # make categorisation B from yaml
    categorisation_b = cc.IPCC2006_PRIMAP

    # category FAOSTAT not yet part of climate categories, so we need to add it manually
    cats = {
        "FAO": categorisation_a,
        "IPCC2006_PRIMAP": categorisation_b,
    }

    # drop UNFCCC data
    ds = ds.drop_sel(source="UNFCCC")

    # consistency check in original categorisation
    ds_checked = ds.pr.add_aggregates_coordinates(agg_info=agg_info_fao, min_count=1)  # noqa: F841

    # We need a conversion CSV file for each entity
    # That's a temporary workaround until the filter function in climate categories works
    conv = {}
    gases = ["CO2", "CH4", "N2O"]

    for var in gases:
        conversion_path = root_path / f"conv_FAO_IPPCC2006_PRIMAP_{var}.csv"
        conv[var] = cc.Conversion.from_csv(
            conversion_path,
            cats=cats,  # type: ignore
        )

    # convert for each entity
    da_dict = {}
    for var in gases:
        da_dict[var] = ds[var].pr.convert(
            dim="category (FAO)",
            conversion=conv[var],
        )

    result = xr.Dataset(da_dict)
    result.attrs = ds.attrs
    result.attrs["cat"] = "category (IPCC2006_PRIMAP)"

    # convert to interchange format and back to get rid of empty categories
    # TODO there may be a better way to do this
    result_if = result.pr.to_interchange_format()
    result = pm2.pm2io.from_interchange_format(result_if)

    # aggregation for each gas for better understanding
    # TODO creates some duplicate code, we can combine again later
    result_proc = result.pr.add_aggregates_coordinates(
        agg_info=agg_info_ipcc2006_primap_N2O, min_count=1
    )

    result_proc = result_proc.pr.add_aggregates_coordinates(
        agg_info=agg_info_ipcc2006_primap_CO2, min_count=1
    )

    result_proc = result_proc.pr.add_aggregates_coordinates(
        agg_info=agg_info_ipcc2006_primap_CH4, min_count=1
    )

    return result_proc  # type: ignore


def read_latest_data(
    downloaded_data_path_custom: pathlib.Path = downloaded_data_path,
    save_path: pathlib.Path = extracted_data_path,
) -> None:
    """
    Read and save the latest data

    Converts downloaded data into interchange format and primap2 native format
    and saves the files in the extracted_data directory.

    """
    domains = get_all_domains(downloaded_data_path_custom)

    domains_and_releases_to_read = []
    for domain in domains:
        domain_path = downloaded_data_path_custom / domain
        domains_and_releases_to_read.append((domain, get_latest_release(domain_path)))

    read_data(
        read_path=downloaded_data_path_custom,
        domains_and_releases_to_read=domains_and_releases_to_read,
        save_path=save_path,
    )
