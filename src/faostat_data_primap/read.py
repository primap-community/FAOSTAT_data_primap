"""read data set"""

import os
import pathlib

import pandas as pd
import primap2 as pm2

from faostat_data_primap.helper.country_mapping import country_to_iso3_mapping
from faostat_data_primap.helper.definitions import (
    config_to_if,
    read_config_all,
)
from faostat_data_primap.helper.paths import (
    downloaded_data_path,
    extracted_data_path,
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


def read_latest_data(
    downloaded_data_path: pathlib.Path = downloaded_data_path,
    save_path: pathlib.Path = extracted_data_path,
) -> None:
    """
    Read and save the latest data

    Converts downloaded data into interchange format and primap2 native format
    and saves the files in the extracted_data directory.

    """
    domains = get_all_domains(downloaded_data_path)

    files_to_read = []
    for domain in domains:
        domain_path = downloaded_data_path / domain
        files_to_read.append((domain, get_latest_release(domain_path)))

    df_all = None
    for domain, release in files_to_read:
        read_config = read_config_all[domain][release]

        print(f"Read {read_config['filename']}")
        dataset_path = downloaded_data_path / domain / release / read_config["filename"]

        # There are some non-utf8 characters
        df_domain = pd.read_csv(dataset_path, encoding="ISO-8859-1")

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
        df_domain["category"] = df_domain["Item"] + "-" + df_domain["Element"]

        # drop columns we don't need
        df_domain = df_domain.drop(
            read_config["columns_to_drop"],
            axis=1,
        )

        if df_all is None:
            df_all = df_domain
        else:
            df_all = pd.concat(
                [df_all, df_domain],
                axis=0,
                join="outer",
            ).reset_index(drop=True)

    # sometimes Source is empty
    df_all["Source"] = df_all["Source"].fillna("unknown")

    # Remove the "Y" prefix for the years columns
    df_all = df_all.rename(columns=lambda x: x.lstrip("Y") if x.startswith("Y") else x)

    # Make sure the units are correct
    df_all["Unit"] = df_all["entity"] + " * " + df_all["Unit"] + "/ year"
    df_all["Unit"] = df_all["Unit"].replace(read_config_all["replace_units"])

    date_last_updated = sorted([i[1] for i in files_to_read], reverse=True)[0]
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
    output_filename = f"FAOSTAT_Agrifood_system_emissions_{release_name}"

    if not extracted_data_path.exists():
        extracted_data_path.mkdir()

    output_folder = save_path / release_name
    if not output_folder.exists():
        output_folder.mkdir()

    pm2.pm2io.write_interchange_format(
        output_folder / (output_filename + ".csv"),
        data_if,
    )

    compression = dict(zlib=True, complevel=9)
    encoding = {var: compression for var in data_pm2.data_vars}
    data_pm2.pr.to_netcdf(output_folder / (output_filename + ".nc"), encoding=encoding)

    # next steps
    # convert to IPCC2006_PRIMAP categories
    # save final version
