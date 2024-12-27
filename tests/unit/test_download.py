import pytest

from src.faostat_data_primap.download import (
    find_previous_release_path,
)


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


@pytest.mark.parametrize(
    "releases," "current_release_date, " "expected_result_date",
    [
        pytest.param(
            ["2023-12-13", "2022-03-18", "2024-11-29", "2024-11-09"],
            "2024-11-29",
            "2024-11-09",
            id="current release is latest release",
        ),
        pytest.param(
            ["2023-12-13", "2022-03-18", "2024-11-29", "2024-11-09"],
            "2023-12-13",
            "2022-03-18",
            id="current somewhere not the latest release",
        ),
    ],
)
def test_find_previous_release_path_exists(
    temp_domain_directories, releases, current_release_date, expected_result_date
):
    domain_path = temp_domain_directories["domain_paths"][
        0
    ]  # farm_gate_emissions_crops
    current_release_path = domain_path / current_release_date
    expected_result = domain_path / expected_result_date

    release_paths = []
    for release in releases:
        release_path = domain_path / release
        release_path.mkdir()
        release_paths.append(release_path)

    result = find_previous_release_path(current_release_path)

    assert result == expected_result


@pytest.mark.parametrize(
    "releases,current_release_date",
    [
        pytest.param(
            ["2023-12-13", "2022-03-18", "2024-11-29", "2024-11-09"],
            "2022-03-18",
            id="current release is oldest release",
        ),
        pytest.param(
            ["2024-11-09"], "2024-11-09", id="current release is only release"
        ),
    ],
)
def test_find_previous_release_path_that_does_not_exists(
    temp_domain_directories, releases, current_release_date
):
    domain_path = temp_domain_directories["domain_paths"][
        0
    ]  # farm_gate_emissions_crops
    current_release_path = domain_path / current_release_date

    release_paths = []
    for release in releases:
        release_path = domain_path / release
        release_path.mkdir()
        release_paths.append(release_path)

    result = find_previous_release_path(current_release_path)

    assert not result


@pytest.mark.parametrize(
    "releases,current_release_date, error_msg",
    [
        pytest.param(
            ["2023-12-13", "2022-03-18", "2024-11-29", "20240-11-09"],
            "2022-03-18",
            (
                "All release folders must be in YYYY-MM-DD format, got "
                "['2022-03-18', '2023-12-13', '2024-11-29', '20240-11-09']"
            ),
            id="typo",
        ),
        pytest.param(
            ["20231213", "2022-03-18", "2024-11-29", "2024-11-09"],
            "2022-03-18",
            (
                "All release folders must be in YYYY-MM-DD format, got "
                "['2022-03-18', '20231213', '2024-11-09', '2024-11-29']"
            ),
            id="missing hyphen",
        ),
    ],
)
def test_find_previous_release_path_wrong_dir_format(
    temp_domain_directories, releases, current_release_date, error_msg
):
    domain_path = temp_domain_directories["domain_paths"][
        0
    ]  # farm_gate_emissions_crops
    current_release_path = domain_path / current_release_date

    release_paths = []
    for release in releases:
        release_path = domain_path / release
        release_path.mkdir()
        release_paths.append(release_path)

    with pytest.raises(ValueError) as excinfo:
        result = find_previous_release_path(current_release_path)  # noqa: F841

    assert str(excinfo.value) == error_msg
