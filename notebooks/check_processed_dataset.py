# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import climate_categories as cc
import plotly.express as px  # type: ignore
import plotly.graph_objects as go  # type: ignore
import primap2 as pm2

from faostat_data_primap.helper.paths import (
    extracted_data_path,
)

# import plotly.graph_objects as go  # type: ignore

# %%
ds_path = (
    extracted_data_path / "v2024-11-14/FAOSTAT_Agrifood_system_emissions_v2024-11-14.nc"
)
ds = pm2.open_dataset(ds_path)

# %%
ds

# %%
entity = "CO2"
filtered = (
    ds[entity]
    .pr.loc[
        {
            "area (ISO3)": ["DEU"],
        }
    ]
    .squeeze()
)

# %%
filtered_pandas = filtered.to_dataframe().reset_index()

# %%
filtered_pandas

# %%
fig = px.area(
    filtered_pandas,
    x="time",
    y="CO2",
    color="category (IPCC2006_PRIMAP)",
    # title="category split"
)

fig.update_layout(
    xaxis=dict(rangeslider=dict(visible=True), type="date"),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
    margin=dict(l=0, r=0, t=0, b=0),  # distance to next element
)

fig.show()

# %%
filtered_pandas["category (IPCC2006_PRIMAP)"].unique()

# %%


# %%
categories_cc = cc.IPCC2006_PRIMAP

# %%
fig = go.Figure()
three_a_cats = [
    "3.A",
    "3.A.1",
    "3.A.1.a",
    "3.A.1.a.i",
    "3.A.1.a.ii",
    "3.A.1.b",
    "3.A.1.c",
    "3.A.1.d",
    "3.A.1.e",
    "3.A.1.f",
    "3.A.1.g",
    "3.A.1.h",
    "3.A.1.j",
    "3.A.2",
    "3.A.2.a",
    "3.A.2.a.i",
    "3.A.2.a.ii",
    "3.A.2.b",
    "3.A.2.c",
    "3.A.2.d",
    "3.A.2.e",
    "3.A.2.f",
    "3.A.2.g",
    "3.A.2.h",
    "3.A.2.i",
    "3.A.2.j",
]
three_b_cats = ["3.B.1", "3.B.2", "3.B.3"]
three_c_cats = [
    "3.C",
    "3.C.1",
    "3.C.1.a",
    "3.C.1.b",
    "3.C.1.c",
    "3.C.4",
    "3.C.5",
    "3.C.6",
    "3.C.7",
]
for cat in three_c_cats:
    filtered_pandas_cat = filtered_pandas.loc[
        filtered_pandas["category (IPCC2006_PRIMAP)"] == cat
    ]

    fig.add_trace(
        go.Scatter(
            x=list(filtered_pandas_cat["time"]),
            y=list(filtered_pandas_cat[entity]),
            # mode=mode,
            marker_symbol="cross",
            marker_size=10,
            name=f"{cat} {categories_cc["3.C.1.b"].title}",
            # line=line_layout,
            # visible=self.source_scenario_visible[source_scenario],
            hovertemplate="%{y:.2e} ",
        )
    )

fig.update_layout(
    xaxis=dict(
        rangeslider=dict(visible=True, thickness=0.05),
        type="date",
    ),
    yaxis=dict(
        autorange=True,
    ),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0),
    margin=dict(l=0, r=0, t=0, b=20),  # distance to next element
    autosize=True,
    hovermode="x",
    yaxis_title=str(ds[entity].data.units),
)

fig.show()

# %%

# %%
