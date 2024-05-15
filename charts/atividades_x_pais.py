import pandas as pd
import plotly.express as px
from dash_util import dash_util, styles

# setup
util = dash_util
dcc = util.dash.dcc
html = util.dash.html


def create_chart(df, title="Produção por atividade"):
    # limpando dados desnecessarios
    df = df.iloc[:, 1:]
    # df.drop("país", axis=1, inplace=True)
    # df.drop("país", axis=1, inplace=True)
    df.drop("categoria", axis=1, inplace=True)
    df["atividade"] = df["atividade"].str.split(",")

    # Melt the DataFrame to have activity as a separate row
    df_melted = pd.melt(
        df,
        id_vars=["país", "atividade"],
        # id_vars=["name", "state", "country", "scope"],
        var_name="Produto",
        value_name="producao",
    )

    df.drop("atividade", axis=1, inplace=True)

    # Group by state and activity and sum the production values
    df_grouped = df_melted.groupby(["país", "Produto"])["producao"].sum().reset_index()

    fig = px.bar(
        df_grouped,
        y="país",
        x="producao",
        color="Produto",
        orientation="h",
        labels={"país": "País", "producao": "Produção", "atividade": "Atividade"},
        color_continuous_scale="viridis",
    )

    fig.update_layout(
        barmode="stack",
        height=800,
        font=dict(size=18),
    )  # Stacked bar chart layout
    return html.Div(
        children=[html.H3(title, className=styles["h3"]), dcc.Graph(figure=fig)],
        className="",
    )
