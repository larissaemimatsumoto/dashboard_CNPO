import pandas as pd
import plotly.express as px
from dash_util import dash_util, styles

# Setup
util = dash_util
app = util.app
dcc = util.dash.dcc
html = util.dash.html
Input = util.dash.Input
Output = util.dash.Output

# Read data
df = pd.read_csv("./dados.csv")

# Get unique list of activities
atividades = df.columns[5:]  # Assuming activities start from column 5

# Define layout
layout = html.Div(
    [
        html.H3("Produtos x UF", className=styles["h3"]),
        html.Div(
            children=[
                html.Label("Produto: "),
                dcc.Dropdown(
                    id="activity-dropdown",
                    options=[
                        {"label": atividade, "value": atividade}
                        for atividade in atividades
                    ],
                    value=atividades[0],  # Set default value to first activity
                    className="text-xl min-w-[14rem]",
                ),
            ],
            className="flex items-center space-x-4 py-4",
        ),
        html.Div(id="chart-container", className="h-[90vh] w-full"),
    ]
)


# Define callback to update chart
@app.callback(
    Output("chart-container", "children"), [Input("activity-dropdown", "value")]
)
def update_chart(selected_activity):
    # print("update_chart triggered with activity:", selected_activity)  # Debugging
    # Group data by UF and sum the counts of the selected activity
    atividade_counts = df.groupby("uf")[selected_activity].sum().reset_index()

    # Plot bubble map using choropleth
    fig = px.choropleth(
        atividade_counts,
        geojson="https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson",
        featureidkey="properties.sigla",
        locations="uf",
        color=selected_activity,
        color_continuous_scale="Viridis",
        title=f"Produtores de {selected_activity.capitalize()} por UF",
    )

    # Update layout
    fig.update_geos(
        visible=True,
        showcountries=False,
        showcoastlines=False,
        showland=False,
        showocean=False,
        showlakes=False,
        showrivers=False,
        showframe=False,
        showsubunits=True,
        subunitcolor="black",
        subunitwidth=1.5,
        fitbounds="geojson",
        # projection_type="natural earth",
    )

    # Update layout to disable scroll zoom and pan
    fig.update_layout(
        dragmode=False,  # Disable pan on click/hold
        uirevision="foo",  # Prevent scroll zoom
    )
    # Return the chart component
    return dcc.Graph(figure=fig, className="h-full w-full")


chart = layout

