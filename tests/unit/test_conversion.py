"""Note that these tests only run locally, because they require the downloaded data"""
import primap2 as pm2
import pytest
import xarray as xr

from faostat_data_primap.helper.paths import (
    downloaded_data_path,
    extracted_data_path,
)
from faostat_data_primap.read import process, read_data


# For development work on process function only
def test_processed_output_remains_the_same():
    # get processed data
    release_name = "v2024-11-14"
    # release_name = "v2023-12-13"
    filename_processed_ds = f"FAOSTAT_Agrifood_system_emissions_{release_name}"
    filepath = extracted_data_path / release_name / (filename_processed_ds + ".nc")
    ds_processed = pm2.open_dataset(filepath)

    # get raw data
    filename_raw_ds = (
        extracted_data_path
        / f"{release_name}/FAOSTAT_Agrifood_system_emissions_{release_name}_raw.nc"
    )
    ds_raw = pm2.open_dataset(filename_raw_ds)

    # process raw data
    ds_processed_new = process(ds=ds_raw)

    # filter by primap categories (sub-categories can change)
    primap_sectors = ["3", "3.A", "M.AG", "M.AG.ELV", "M.LULUCF"]
    ds_processed = ds_processed.loc[{"category (IPCC2006_PRIMAP)": primap_sectors}]
    ds_processed_new = ds_processed_new.loc[
        {"category (IPCC2006_PRIMAP)": primap_sectors}
    ]

    # compare
    xr.testing.assert_allclose(
        ds_processed, ds_processed_new, rtol=1e-10, check_dim_order=False
    )

    # assert ds_processed.broadcast_equals(ds_processed_new)


@pytest.mark.parametrize(
    "domains_and_releases_to_read",
    [
        pytest.param(
            [
                ("farm_gate_agriculture_energy", "2023-12-13"),
                ("farm_gate_emissions_crops", "2023-11-09"),
                ("farm_gate_livestock", "2023-11-09"),
                ("land_use_drained_organic_soils", "2023-11-09"),
                ("land_use_fires", "2023-11-09"),
                ("land_use_forests", "2023-11-09"),
                ("pre_post_agricultural_production", "2023-11-09"),
            ],
            id="2023 release",
        ),
        pytest.param(
            [
                ("farm_gate_agriculture_energy", "2024-11-14"),
                ("farm_gate_emissions_crops", "2024-11-14"),
                ("farm_gate_livestock", "2024-11-14"),
                ("land_use_drained_organic_soils", "2024-11-14"),
                ("land_use_fires", "2024-11-14"),
                ("land_use_forests", "2024-11-14"),
                ("pre_post_agricultural_production", "2024-11-14"),
            ],
            id="2024 release",
        ),
    ],
)
def test_read(tmp_path, domains_and_releases_to_read):
    read_data(
        domains_and_releases_to_read=domains_and_releases_to_read,
        read_path=downloaded_data_path,
        save_path=tmp_path,
        # save_path=extracted_data_path,
    )


# TODO delete everything below here when data set is final
# def test_conversion_from_FAO_to_IPCC2006_PRIMAP():
#     release_name = "v2024-11-14"
#     # release_name = "v2023-12-13"
#
#     # get raw data
#     filename_raw_ds = (
#         extracted_data_path
#         / f"{release_name}/FAOSTAT_Agrifood_system_emissions_{release_name}_raw.nc"
#     )
#     ds_raw = pm2.open_dataset(filename_raw_ds)
#
#     # process raw data
#     result_proc = process(ds=ds_raw)
#
#     result_proc_if = result_proc.pr.to_interchange_format()
#
#     # save processed data
#     output_filename = f"FAOSTAT_Agrifood_system_emissions_{release_name}"
#     output_folder = extracted_data_path / release_name
#
#     if not output_folder.exists():
#         output_folder.mkdir()
#
#     filepath = output_folder / (output_filename + ".csv")
#     print(f"Writing processed primap2 file to {filepath}")
#     pm2.pm2io.write_interchange_format(
#         filepath,
#         result_proc_if,
#     )
#
#     compression = dict(zlib=True, complevel=9)
#     encoding = {var: compression for var in result_proc.data_vars}
#     filepath = output_folder / (output_filename + ".nc")
#     print(f"Writing netcdf file to {filepath}")
#     result_proc.pr.to_netcdf(filepath, encoding=encoding)
#
# def test_read_2023():
#     domains_and_releases_to_read = [
#         # ("farm_gate_agriculture_energy", "2023-12-13"),
#         # ("farm_gate_emissions_crops", "2023-11-09"),
#         # ("farm_gate_livestock", "2023-11-09"),
#         # ("land_use_drained_organic_soils", "2023-11-09"),
#         # ("land_use_fires", "2023-11-09"),
#         # ("land_use_forests", "2023-11-09"),
#         # ("pre_post_agricultural_production", "2023-11-09"),
#         ("farm_gate_agriculture_energy", "2024-11-14"),
#         ("farm_gate_emissions_crops", "2024-11-14"),
#         ("farm_gate_livestock", "2024-11-14"),
#         ("land_use_drained_organic_soils", "2024-11-14"),
#         ("land_use_fires", "2024-11-14"),
#         ("land_use_forests", "2024-11-14"),
#         ("pre_post_agricultural_production", "2024-11-14"),
#     ]
#
#     read_data(
#         domains_and_releases_to_read=domains_and_releases_to_read,
#         read_path=downloaded_data_path,
#         save_path=extracted_data_path,
#     )
