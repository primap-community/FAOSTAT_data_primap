"""read data set"""
import os

import pandas as pd

from src.faostat_data_primap.helper.definitions import downloaded_data_path

# read everything into data frames
# loop through all domains, but not the relases
# always use the latest release
domain = "farm_gate_agriculture_energy"
release = "2024-11-14"
dataset_path = downloaded_data_path / domain / release
all_data = {}
for item in os.listdir(dataset_path):
    if item.endswith(".csv"):
        all_data[item] = pd.read_csv(dataset_path / item)

# Steps:
# delete columns that are not needed
# map country names to country ISO3 codes
# convert to interchange format
# convert to primap2 format
# save raw data set
# convert categories to IPCC2006_PRIMAP standard
# save data set
