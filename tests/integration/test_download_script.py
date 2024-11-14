import os

from src.faostat_data_primap.download import download_all_domains


# test the whole download script run
def test_download_all_domains(tmp_path):
    downloaded_data_path = tmp_path / "downloaded_data"
    download_all_domains(downloaded_data_path=downloaded_data_path)

    expected_downloaded_domains = [
        "farm_gate_emissions_crops",
        "farm_gate_livestock",
        "farm_gate_agriculture_energy",
        "land_use_forests",
        "land_use_fires",
        "land_use_drained_organic_soils",
        "pre_post_agricultural_production",
    ]

    domains = []
    for domain in downloaded_data_path.iterdir():
        if domain.is_dir():
            domains.append(domain.name)
        for release in domain.iterdir():
            downloaded_data = os.listdir(release)
            # make sure we have at least one .csv, one .pdf and one .zip file
            assert [f for f in downloaded_data if f.endswith(".csv")]
            assert [f for f in downloaded_data if f.endswith(".pdf")]
            assert [f for f in downloaded_data if f.endswith(".zip")]

    assert sorted(expected_downloaded_domains) == sorted(domains)
