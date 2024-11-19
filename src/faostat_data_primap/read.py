"""read data set"""

import pandas as pd
import primap2 as pm2
import pycountry

from src.faostat_data_primap.helper.definitions import (
    downloaded_data_path,
    read_config_all,
country_to_iso3_mapping,
)

# mapping = pd.read_csv("../../FAOSTAT_data_11-19-2024.csv")#, encoding="ISO-8859-1")
# mapping_dict = {}
# for idx, row in mapping.iterrows():
#     mapping_dict[row['Country']] = row['ISO3 Code']


# custom_country_mapping_code = {}
# custom_country_mapping_name = {
#     # farm gate agricultur energy
#     "Bolivia (Plurinational State of)": "BOL",
#     "China, Hong Kong SAR": "HKG",
#     "China, Macao SAR": "MAC",
#     "China, mainland": "CHN",
#     "China, Taiwan Province of": "TWN",
#     "Iran (Islamic Republic of)": "IRN",
#     "Czechoslovakia": "CSK",
#     "Ethiopia PDR": "ETH",
#     "Netherlands (Kingdom of the)": "NLD",
#     "Netherlands Antilles (former)": "ANT",
#     # todo is former Sudan same as the new (north) Sudan
#     "Sudan (former)": "SDN",
#     "USSR": "SUN",
#     "Venezuela (Bolivarian Republic of)": "VEN",
#     "Yugoslav SFR": "YUG",
#     "World": "EARTH",
#     # todo Andrews cement list below (deleted commented lines)
#     # "Bonaire, Saint Eustatius and Saba": "BES",
#     # "Cape Verde": "CPV",
#     "Democratic Republic of the Congo": "COD",
#     # "Faeroe Islands": "FRO",
#     "Micronesia (Federated States of)": "FSM",
#     # "Iran": "IRN",
#     # "Laos": "LAO",
#     # "Occupied Palestinian Territory": "PSE",
#     # "Swaziland": "SWZ",
#     # "Taiwan": "TWN",
#     "Wallis and Futuna Islands": "WLF",
#     # farm gate emissions crops
#     "United States Virgin Islands": "VIR",
#     # todo is this relevant to us?
#     "Pacific Islands Trust Territory": "PIC",
#     "Svalbard and Jan Mayen Islands": "SJM",  # Norwy
#     # something goes wrong with french characters in land_use_forest
#     "CÃ´te d'Ivoire": "CIV",
#     "CuraÃ§ao": "CUW",
#     "RÃ©union": "REU",
#     "TÃ¼rkiye": "TUR",
#     # pycountry mixes up these
#     'Niger' : 'NER',
#     'Nigeria' : 'NGA',
#     "Curaçao" : "CUW",
#     "Republic of Korea" : 'KOR',
#     "Democratic People's Republic of Korea" : "PRK",
# }

#
# def get_country_code(
#     country_name: str,
# ) -> str:
#     """
#     Get country code for country name.
#
#     If the input is a code it will be returned,
#     if the input is not a three-letter code a search will be performed
#
#     Parameters
#     ----------
#     country_name: str
#         Country code or name to get the three-letter code for.
#
#     Returns
#     -------
#         country_code: str
#
#     """
#     # First check if it's in the list of custom codes
#     if country_name in custom_country_mapping_code:
#         country_code = country_name
#     elif country_name in custom_country_mapping_name:
#         country_code = custom_country_mapping_name[country_name]
#     else:
#         try:
#             # check if it's a 3 letter UNFCCC_GHG_data
#             country = pycountry.countries.get(alpha_3=country_name)
#             country_code = country.alpha_3
#         except:
#             try:
#                 country = pycountry.countries.search_fuzzy(
#                     country_name.replace("_", " ")
#                 )
#             except:
#                 msg = f"Cannot map country {country_name} to country code."
#                 raise ValueError(msg)
#             if len(country) > 1:
#                 country_code = None
#                 for current_country in country:
#                     if current_country.name == country_name:
#                         country_code = current_country.alpha_3
#                 if country_code is None:
#                     msg = (
#                         f"Country name {country_name} has {len(country)} "
#                         "possible results for country codes."
#                     )
#                     raise ValueError(msg)
#
#             country_code = country[0].alpha_3
#
#     return country_code


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
    df_domain = pd.read_csv(dataset_path, encoding='ISO-8859-1')

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

    # check for duplicates (same data, different country name)
    # duplicates = df_domain.copy().drop(labels=["Area", "Area Code (M49)", "Area Code"], axis=1)
    # duplicates = duplicates[duplicates.duplicated(keep=False)]
    # if not duplicates.empty:
    #     msg = f"Duplicate values for {domain}"
    #     raise ValueError(msg)

    # country name to ISO3 country code mapping
    # countries_to_map = [
    #     c for c in df_domain["Area"].unique() if c not in country_mapping.keys()
    # ]
    # for country_to_map in countries_to_map:
    #     country_mapping[country_to_map] = get_country_code(country_to_map)

    # make sure we don't map duplicate country codes
    # if len(country_mapping.values()) != len(set(country_mapping.values())):
    #     duplicate_codes = [x for i, x in enumerate(list(country_mapping.values())) if list(country_mapping.values()).count(x) > 1]
    #     duplicates = [(key, value) for (key, value) in country_mapping.items() if value in duplicate_codes]
    #     msg = f"Duplicate country codes for {domain}. Check country_mapping"
    #     raise ValueError(msg)



    # create country columns
    df_domain["country (ISO3)"] = df_domain["Area"].map(country_to_iso3_mapping)

    # check all countries are converted into iso3 codes
    if any(df_domain['country (ISO3)'].isna()):
        raise ValueError

    # check for duplicates (same data, different country name)
    # duplicates = df_domain.copy().drop(labels=["Area", "Area Code (M49)", "Area Code"], axis=1)
    # duplicates = duplicates[duplicates.duplicated(keep=False)]
    # if not duplicates.empty:
    #     msg = f"Duplicate values for {domain}. Check country {duplicates['country (ISO3)'].unique()}"
    #     raise ValueError(msg)

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

coords_cols = {
    "area": "country (ISO3)",
    "unit": "Unit",
    "entity": "entity",
    "source": "Source",
}

coords_terminologies = {"area": "ISO3", "category": "FAOSTAT"}

coords_defaults = {
    # "source": "FAO",
    "scenario": release,
}

coords_value_mapping = {}
filter_keep = {}
filter_remove = {}
meta_data = {
    "references": "tbd",
    "rights": "tbd",
    "contact": "tbd",
    "title": "tbd",
    "comment": "tbd",
    "institution": "tbd",
}
# Rename columns to remove the "Y" prefix
df_all.rename(columns=lambda x: x.lstrip('Y') if x.startswith('Y') else x, inplace=True)

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

pass
# steps:
# convert to primap2 format
# save raw data set
# convert categories to IPCC2006_PRIMAP standard
# save data set
