import pytest
import requests

from src.faostat_data_primap.download import (
    calculate_checksum,
    download_methodology,
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
    "releases,current_release_date",
    [
        pytest.param(
            ["2023-12-13", "2022-03-18", "2024-11-29", "20240-11-09"],
            "2022-03-18",
            id="typo",
        ),
        pytest.param(
            ["20231213", "2022-03-18", "2024-11-29", "2024-11-09"],
            "2022-03-18",
            id="missing hyphen",
        ),
    ],
)
def test_find_previous_release_path_wrong_dir_format(
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

    with pytest.raises(ValueError) as excinfo:
        result = find_previous_release_path(current_release_path)  # noqa: F841

    assert str(excinfo.value) == "All release folders must be in YYYY-MM-DD format"


def test_calculate_checksum(tmp_path):
    filepath_a = tmp_path / "test_file_a.txt"
    with open(filepath_a, "w") as f:
        f.write("content of file a")

    filepath_b = tmp_path / "test_file_b.txt"
    with open(filepath_b, "w") as f:
        f.write("content of file a")

    filepath_c = tmp_path / "test_file_c.txt"
    with open(filepath_c, "w") as f:
        f.write("content of file c")

    checksum_a = calculate_checksum(filepath_a)

    checksum_b = calculate_checksum(filepath_b)

    checksum_c = calculate_checksum(filepath_c)

    assert checksum_a == checksum_b

    assert checksum_b != checksum_c


def test_file_exists_in_previous_release_and_is_the_same(temp_domain_directories):
    # set up temporary directories
    downloaded_data_path = temp_domain_directories["downloaded_data"]
    domain_path = temp_domain_directories["domain_paths"][
        0
    ]  # farm_gate_emissions_crops

    # make folders for different releases
    for release in ["2023-12-13", "2022-03-18", "2024-11-29", "2024-11-09"]:
        release_path = domain_path / release
        release_path.mkdir()

    file_to_compare_path = domain_path / "2024-11-09" / "GCE_e.pdf"
    response = requests.get(
        "https://files-faostat.fao.org/production/GCE/GCE_e.pdf",
        stream=True,
        timeout=30,
    )
    response.raise_for_status()  # Check for successful request
    with open(file_to_compare_path, "wb") as f:
        f.write(response.content)
    save_path = downloaded_data_path / "farm_gate_emissions_crops" / "2024-11-29"
    download_methodology(
        "https://files-faostat.fao.org/production/GCE/GCE_e.pdf", save_path=save_path
    )
    downloaded_file_path = domain_path / "2024-11-29" / "GCE_e.pdf"
    assert downloaded_file_path.is_symlink()


def test_methodology_document_exists_in_previous_release_but_is_different(
    temp_domain_directories,
):
    # set up temporary directories
    domain_path = temp_domain_directories["domain_paths"][
        0
    ]  # farm_gate_emissions_crops

    # make folders for different releases
    for release in ["2023-12-13", "2022-03-18", "2024-11-29", "2024-11-09"]:
        release_path = domain_path / release
        release_path.mkdir()

    file_to_compare_path = domain_path / "2024-11-09" / "GCE_e.pdf"
    with open(file_to_compare_path, "wb") as f:
        s = "hi"
        f.write(s.encode("utf-8"))

    save_path = domain_path / "2024-11-29"
    download_methodology(
        "https://files-faostat.fao.org/production/GCE/GCE_e.pdf", save_path=save_path
    )
    downloaded_file_path = domain_path / "2024-11-29" / "GCE_e.pdf"
    assert downloaded_file_path.exists()


def test_methodology_document_does_not_exist_in_previous_release(
    temp_domain_directories,
):
    # set up temporary directories
    domain_path = temp_domain_directories["domain_paths"][
        0
    ]  # farm_gate_emissions_crops

    # make folders for different releases
    for release in ["2023-12-13", "2022-03-18", "2024-11-29", "2024-11-09"]:
        release_path = domain_path / release
        release_path.mkdir()

    save_path = domain_path / "2024-11-29"
    download_methodology(
        "https://files-faostat.fao.org/production/GCE/GCE_e.pdf", save_path=save_path
    )
    downloaded_file_path = domain_path / "2024-11-29" / "GCE_e.pdf"
    assert downloaded_file_path.exists()
