import pytest


@pytest.fixture
def temp_domain_directories(tmp_path):
    """
    Sets up a temporary directory structure for domains and releases for testing.

    Parameters
    ----------
    tmp_path : pathlib.Path
        A pytest-provided temporary directory path.

    Returns
    -------
    dict
        A dictionary containing the paths to the `downloaded_data` directory,
        the specific domain directory, and a list of sorted release paths.
    """
    downloaded_data = tmp_path / "downloaded_data"
    downloaded_data.mkdir()

    domains = (
        "farm_gate_emissions_crops",
        "farm_gate_livestock",
        "farm_gate_agriculture_energy",
        "land_use_forests",
        "land_use_fires",
        "land_use_drained_organic_soils",
        "pre_post_agricultural_production",
    )
    domain_paths = []

    for domain in domains:
        domain_path = downloaded_data / domain
        domain_path.mkdir()
        domain_paths.append(domain_path)

    return {
        "downloaded_data": downloaded_data,
        "domain_paths": domain_paths,
    }
