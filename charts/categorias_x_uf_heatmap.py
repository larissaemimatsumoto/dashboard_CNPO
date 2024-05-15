import pandas as pd
import plotly.express as px
from dash_util import dash_util, styles

# setup
util = dash_util
dcc = util.dash.dcc
html = util.dash.html

df = pd.read_csv("./dados_br.csv")

# Create a DataFrame for the heatmap
df_2dhist = pd.DataFrame(
    {
        uf: df[df["uf"] == uf]["categoria"].str.split(", ").explode().value_counts()
        for uf in df["uf"].unique()
    }
)

# Fill NaN values with 0
df_2dhist.fillna(0, inplace=True)

# Convert count values to integers and truncate
df_2dhist = df_2dhist.astype(int)

# Transpose the DataFrame
df_2dhist = df_2dhist.T

# Plotting using Plotly
fig = px.imshow(
    df_2dhist,
    labels=dict(x="Categoria", y="UF", color="Count"),
    x=df_2dhist.columns,
    y=df_2dhist.index,
    color_continuous_scale="viridis",
    aspect="auto",
)

# Add count values directly on the cells using annotations
for i in range(len(df_2dhist.index)):
    for j in range(len(df_2dhist.columns)):
        count_value = df_2dhist.values[i][j]
        if count_value != 0:  # Display count values only if non-zero
            fig.add_annotation(
                x=df_2dhist.columns[j],
                y=df_2dhist.index[i],
                text=int(count_value),  # Truncate and convert to int
                showarrow=False,
                font=dict(color="white"),  # Set font color
                xshift=-5,  # Adjust x position for better alignment
            )

# TODO - Fix chart size
fig.update_layout(
    xaxis=dict(title="Categoria"),
    yaxis=dict(title="UF"),
    height=800,
    font=dict(size=18),
)
chart = html.Div(
    children=[
        html.H3("Categorias x UF", className=styles["h3"]),
        dcc.Graph(figure=fig),
    ],
    className="w-full",
)
# chart = dcc.Graph(figure=fig)
