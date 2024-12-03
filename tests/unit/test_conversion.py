import climate_categories as cc
import primap2 as pm2
import pytest


@pytest.mark.xfail
def test_conversion_from_FAO_to_IPCC2006_PRIMAP():
    # make categorisation A from yaml
    categorisation_a = cc.from_yaml("FAO.yaml")

    # make categorisation B from yaml
    categorisation_b = cc.IPCC2006_PRIMAP

    # categories not part of climate categories so we need to add them manually
    cats = {
        "A": categorisation_a,
        "B": categorisation_b,
    }

    # make conversion from csv
    conv = cc.Conversion.from_csv("conversion.FAO.IPPCC2006_PRIMAP.csv", cats=cats)

    ds = pm2.open_dataset(
        "extracted_data/v2024-11-14/FAOSTAT_Agrifood_system_emissions_v2024-11-14.nc"
    )

    result = ds.pr.convert(
        dim="category",
        conversion=conv,
        auxiliary_dimensions={"gas": "source (gas)"},
    )

    assert result
