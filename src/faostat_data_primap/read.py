"""read data set"""


import pandas as pd
import primap2 as pm2
import pycountry

from src.faostat_data_primap.helper.definitions import downloaded_data_path

custom_country_mapping_code = {}

custom_country_mapping_name = {
    # FAO
    "Bolivia (Plurinational State of)": "BOL",
    "China, Hong Kong SAR": "HKG",
    "China, Macao SAR": "MAC",
    "China, mainland": "CHN",
    "China, Taiwan Province of": "TWN",
    "Iran (Islamic Republic of)": "IRN",
    "Czechoslovakia": "CSK",
    "Ethiopia PDR": "ETH",
    "Netherlands (Kingdom of the)": "NLD",
    "Netherlands Antilles (former)": "ANT",
    # todo is former Sudan same as the new (north) Sudan
    "Sudan (former)": "SDN",
    "USSR": "SUN",
    "Venezuela (Bolivarian Republic of)": "VEN",
    "Yugoslav SFR": "YUG",
    "World": "EARTH",
    # Andrew cement (probably not needed)
    "Bonaire, Saint Eustatius and Saba": "BES",
    "Cape Verde": "CPV",
    "Democratic Republic of the Congo": "COD",
    "Faeroe Islands": "FRO",
    "Micronesia (Federated States of)": "FSM",
    "Iran": "IRN",
    "Laos": "LAO",
    "Occupied Palestinian Territory": "PSE",
    "Swaziland": "SWZ",
    "Taiwan": "TWN",
    "Wallis and Futuna Islands": "WLF",
}


def get_country_code(
    country_name: str,
) -> str:
    """
    Get country code for country name.

    If the input is a code it will be returned,
    if the input is not a three-letter code a search will be performed

    Parameters
    ----------
    country_name: str
        Country code or name to get the three-letter code for.

    Returns
    -------
        country_code: str

    """
    # First check if it's in the list of custom codes
    if country_name in custom_country_mapping_code:
        country_code = country_name
    elif country_name in custom_country_mapping_name:
        country_code = custom_country_mapping_name[country_name]
    else:
        try:
            # check if it's a 3 letter UNFCCC_GHG_data
            country = pycountry.countries.get(alpha_3=country_name)
            country_code = country.alpha_3
        except:
            try:
                country = pycountry.countries.search_fuzzy(
                    country_name.replace("_", " ")
                )
            except:
                msg = f"Cannot map country {country_name} to country code."
                raise ValueError(msg)
            if len(country) > 1:
                country_code = None
                for current_country in country:
                    if current_country.name == country_name:
                        country_code = current_country.alpha_3
                if country_code is None:
                    msg = (
                        f"Country name {country_name} has {len(country)} "
                        "possible results for country codes."
                    )
                    raise ValueError(msg)

            country_code = country[0].alpha_3

    return country_code


files_to_read = (
    (
        "farm_gate_agriculture_energy",
        "2024-11-14",
        "Emissions_Agriculture_Energy_E_All_Data_NOFLAG.csv",
    ),
    (
        "farm_gate_emissions_crops",
        "2024-11-14",
        "Emissions_crops_E_All_Data_NOFLAG.csv",
    ),
)

for domain, release, filename in files_to_read:
    dataset_path = downloaded_data_path / domain / release / filename
    data_pd = pd.read_csv(dataset_path)

    # remove in entries with unit TJ
    data_pd = data_pd[data_pd["Unit"] != "TJ"]

    # remove the country aggegrates
    areas_to_remove = [
        "World",
        "Africa",
        "Eastern Africa",
        "Middle Africa",
        "Northern Africa",
        "Southern Africa",
        "Western Africa",
        "Americas",
        "Northern America",
        "Central America",
        "Caribbean",
        "South America",
        "Asia",
        "Central Asia",
        "Eastern Asia",
        "Southern Asia",
        "South-eastern Asia",
        "Western Asia",
        "Europe",
        "Eastern Europe",
        "Northern Europe",
        "Southern Europe",
        "Western Europe",
        "Oceania",
        "Australia and New Zealand",
        "Melanesia",
        "Micronesia",
        "Polynesia",
        "Least Developed Countries",
        "Land Locked Developing Countries",
        "Small Island Developing States",
        "Low Income Food Deficit Countries",
        "Net Food Importing Developing Countries",
        "Annex I countries",
        "Non-Annex I countries",
        "OECD",
    ]

    data_pd = data_pd[~data_pd["Area"].isin(areas_to_remove)]
    country_mapping = {c: get_country_code(c) for c in data_pd["Area"].unique()}

    data_pd["country (ISO3)"] = data_pd["Area"].map(country_mapping)

    entity_mapping = {
        "Emissions (CO2)": "CO2",
        "Emissions (CH4)": "CH4",
        "Emissions (N2O)": "N2O",
    }

    data_pd["entity"] = data_pd["Element"].map(entity_mapping)

    # todo can we do this in primap2 function?
    data_pd = data_pd.drop(
        ["Element", "Element Code", "Item Code", "Area Code (M49)", "Area Code"], axis=1
    )


coords_cols = {
    "area": "country (ISO3)",
    "category": "Item",
    "unit": "Unit",
    "entity": "entity",
}

coords_terminologies = {"area": "ISO3", "category": "FAOSTAT"}

coords_defaults = {
    "source": "FAO",
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

data_if = pm2.pm2io.convert_wide_dataframe_if(
    data_pd,
    coords_cols=coords_cols,
    coords_defaults=coords_defaults,
    coords_terminologies=coords_terminologies,
    coords_value_mapping=coords_value_mapping,
    filter_keep=filter_keep,
    filter_remove=filter_remove,
    meta_data=meta_data,
)

# steps:
# convert to primap2 format
# save raw data set
# convert categories to IPCC2006_PRIMAP standard
# save data set
