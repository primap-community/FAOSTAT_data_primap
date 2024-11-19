"""read data set"""

import pandas as pd
import primap2 as pm2

from src.faostat_data_primap.helper.definitions import (
    country_to_iso3_mapping,
    downloaded_data_path,
    read_config_all,
)

files_to_read = (
    (
        "farm_gate_agriculture_energy",
        "2024-11-14",
    ),
    (
        "farm_gate_emissions_crops",
        "2024-11-14",
    ),
    (
        "farm_gate_livestock",
        "2024-11-14",
    ),
    (
        "land_use_drained_organic_soils",
        "2023-11-09",
    ),
    (
        "land_use_fires",
        "2023-11-09",
    ),
    (
        "land_use_forests",
        "2024-11-14",
    ),
    (
        "pre_post_agricultural_production",
        "2023-11-09",
    ),
)

df_all = None
country_mapping = {}
# todo remove reversed, I'm using it to get the new domain first in the debugger
for domain, release in reversed(files_to_read):
    read_config = read_config_all[domain][release]

    print(f"Read {read_config["filename"]}")
    dataset_path = downloaded_data_path / domain / release / read_config["filename"]
    # There are some non-utf8 characters in Emissions_Drained_Organic_Soils_E_All_Data_NOFLAG.csv
    df_domain = pd.read_csv(dataset_path, encoding="ISO-8859-1")

    # remove rows by unit
    # todo this is maybe not a good idea as it hides the elements to be removed
    if "units_to_remove" in read_config.keys():
        df_domain = df_domain[~df_domain["Unit"].isin(read_config["units_to_remove"])]

    # remove rows by element
    if "elements_to_remove" in read_config.keys():
        df_domain = df_domain[
            ~df_domain["Element"].isin(read_config["elements_to_remove"])
        ]

    # remove rows by area
    if "areas_to_remove" in read_config.keys():
        df_domain = df_domain[~df_domain["Area"].isin(read_config["areas_to_remove"])]

    # create country columns
    df_domain["country (ISO3)"] = df_domain["Area"].map(country_to_iso3_mapping)

    # check all countries are converted into iso3 codes
    if any(df_domain["country (ISO3)"].isna()):
        raise ValueError

    # create entity column
    df_domain["entity"] = df_domain["Element"].map(read_config["entity_mapping"])

    # create category column (combination of Item and Element works best)
    df_domain["category"] = df_domain["Item"] + " " + df_domain["Element"]

    # drop columns we don't need
    df_domain = df_domain.drop(
        read_config["columns_to_drop"],
        axis=1,
    )

    if df_all is None:
        df_all = df_domain
    else:
        # makes sure there are no duplicate category names
        if any(
            [
                category in df_all["category"].unique()
                for category in df_domain["category"].unique()
            ]
        ):
            msg = f"Duplicate category names for {domain}"
            raise ValueError(msg)
        df_all = pd.concat(
            [df_all, df_domain],
            axis=0,
            join="outer",
        ).reset_index(drop=True)

# df_all = df_all.drop(labels=["Source"], axis=1)
df_all["Source"] = df_all["Source"].fillna("unknown")
coords_cols = {
    "area": "country (ISO3)",
    "unit": "Unit",
    "entity": "entity",
    "source": "Source",
    "category" : "category"
}

coords_terminologies = {"area": "ISO3", "category": "FAOSTAT", "scenario": "FAO"}

coords_defaults = {
    # "source": "FAO",
    "scenario": release,
}

coords_value_mapping = {}
filter_keep = {}
filter_remove = {}
meta_data = {
    "references": "https://www.fao.org/faostat",
    "rights": "Creative Commons Attribution-4.0 International licence (CC BY 4.0)",
    "contact": "daniel.busch@climate-resource.com",
    "title": "Agrifood systems emissions",
    "comment": (
        "Published by Food and Agriculture Organization of the "
        "United Nations (FAO), converted to PRIMAP2 format by "
        "Daniel Busch"
    ),
    "institution": ("Food and Agriculture Organization of the United Nations"),
}
# Rename columns to remove the "Y" prefix
df_all = df_all.rename(columns=lambda x: x.lstrip("Y") if x.startswith("Y") else x)
df_all[df_all["entity"].isin(['FGASES (AR5GWP100)', 'KYOTOGHG (AR5GWP100)'])]["unit"]


data_if = pm2.pm2io.convert_wide_dataframe_if(
    df_all,
    coords_cols=coords_cols,
    coords_defaults=coords_defaults,
    coords_terminologies=coords_terminologies,
    coords_value_mapping=coords_value_mapping,
    filter_keep=filter_keep,
    filter_remove=filter_remove,
    meta_data=meta_data,
)

# convert to PRIMAP2 native format
data_pm2 = pm2.pm2io.from_interchange_format(data_if, data_if.attrs)

# convert back to IF for standardized units
data_if = data_pm2.pr.to_interchange_format()