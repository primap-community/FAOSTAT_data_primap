"""Downloads all domain data sets from FAOSTAT website."""

from faostat_data_primap.download import (
    download_file,
    download_methodology,
    get_html_content,
    get_last_updated_date,
    unzip_file,
)
from faostat_data_primap.helper.definitions import domains, downloaded_data_path


def download_all_domains(sources: list[tuple[str]]) -> list[str]:
    """
    Download and unpack all climate-related domains from the FAO stat website.

    Extract the date when the data set was last updated and create a directory
    with the same name. Download the zip files for each domain if
    it does not already exist. Unpack the zip file and save in
    the same directory.

    Parameters
    ----------
    sources
        Name of data set, url to domain overview,
        and download url

    Returns
    -------
        List of input files that have been fetched or found locally.

    """
    downloaded_files = []
    for ds_name, urls in domains.items():
        url = urls["url_domain"]
        url_download = urls["url_download"]
        url_methodology = urls["url_methodology"]

        soup = get_html_content(url)

        last_updated = get_last_updated_date(soup, url)

        if not downloaded_data_path.exists():
            downloaded_data_path.mkdir()

        ds_path = downloaded_data_path / ds_name
        if not ds_path.exists():
            ds_path.mkdir()

        local_data_dir = ds_path / last_updated
        if not local_data_dir.exists():
            local_data_dir.mkdir()

        download_methodology(save_path=local_data_dir, url_download=url_methodology)

        local_filename = local_data_dir / f"{ds_name}.zip"

        download_file(url_download=url_download, save_path=local_filename)

        downloaded_files.append(str(local_filename))

        unzip_file(local_filename)

    return downloaded_files


if __name__ == "__main__":
    download_all_domains(domains)
