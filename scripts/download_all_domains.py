"""Downloads all domain data sets from FAOSTAT website."""

from src.faostat_data_primap.download import (
    download_file,
    get_html_content,
    get_last_updated_date,
    unzip_file,
)
from src.faostat_data_primap.helper.definitions import downloaded_data_path, sources


def download_all_domains(sources: list[tuple[str]]):
    """
    Download input files from a remote location

    Parameters
    ----------
    download_path
        Name of data set, url to domain overview,
        and download url

    Returns
    -------
        List of input files that have been fetched or found locally.

    """
    downloaded_files = []
    for (
        ds_name,
        url,
        url_download,
    ) in sources:
        soup = get_html_content(url)

        # todo Remove url input
        last_updated = get_last_updated_date(soup, url)

        if not downloaded_data_path.exists():
            downloaded_data_path.mkdir()

        ds_path = downloaded_data_path / ds_name
        if not ds_path.exists():
            ds_path.mkdir()

        local_data_dir = ds_path / last_updated

        if not local_data_dir.exists():
            local_data_dir.mkdir()

        local_filename = local_data_dir / f"{ds_name}.zip"

        download_file(url_download=url_download, save_path=local_filename)

        downloaded_files.append(str(local_filename))

        unzip_file(local_filename)

    return downloaded_files


if __name__ == "__main__":
    download_all_domains(sources)