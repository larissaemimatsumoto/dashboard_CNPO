import numpy as np
import pandas as pd
import geopandas as gpd
from ipywidgets import interact, widgets
import matplotlib.pyplot as plt

df = pd.read_csv("./dados.csv")
brazil_map = gpd.read_file("./BR_UF_2022.shx")

# Drop Roraima
brazil_map = brazil_map.drop(index=26)

uf = pd.Series(
    np.array(
        [
            "AC",
            "AM",
            "PA",
            "AP",
            "TO",
            "MA",
            "PI",
            "CE",
            "RN",
            "PB",
            "PE",
            "AL",
            "SE",
            "BA",
            "MG",
            "ES",
            "RJ",
            "SP",
            "PR",
            "SC",
            "RS",
            "MS",
            "MT",
            "GO",
            "DF",
            "RO",
        ]
    )
)

brazil_map = brazil_map.assign(uf=uf)


atividade_str = df["atividade"].apply(lambda x: x.split(","))

unique_atividade = set()
for atv in atividade_str:
    unique_atividade.update(atv)

unique_atividade = [x for x in unique_atividade if x != "" and x != " "]


def plot_counts_map(product_name, data):
    # Plot the map
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    data.plot(
        column=product_name,
        cmap="viridis",
        linewidth=0.8,
        ax=ax,
        edgecolor="0.8",
        legend=True,
    )
    ax.set_title(f"Número de produtores de {product_name.title()} por Estado no Brasil")


atividade_freq = df.groupby("uf")[unique_atividade].sum()
atividade_freq = pd.DataFrame(atividade_freq)

# Merge the Brazil map with product counts data
atv_merged_data = brazil_map.merge(
    atividade_freq, how="left", left_on="uf", right_on="uf"
)

# Reorder the columns
atv_merged_data = atv_merged_data[
    ["uf", "geometry"]
    + [col for col in atv_merged_data.columns if col not in ["uf", "geometry"]]
]


# Create a product selector dropdown
product_selector = widgets.Dropdown(
    options=sorted(unique_atividade), description="Produção:", disabled=False
)

# Show the map based on the selected product
interact(lambda name: plot_counts_map(name, atv_merged_data), name=product_selector)
