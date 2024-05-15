import pandas as pd
import plotly.express as px
from dash_util import DashUtil

util = DashUtil()
app = util.app
dcc = util.dash.dcc
html = util.dash.html
Input = util.dash.Input
Output = util.dash.Output

# Load data
df = pd.read_csv("./dados.csv")

# Get unique list of activities
atividades = df.columns[5:]  # Assuming activities start from column 5

# Define Dash layout
chart = html.Div(
    [
        html.H1("Brazilian State Bubble Map"),
        html.Label("Select Activity:"),
        dcc.Dropdown(
            id="activity-dropdown",
            options=[
                {"label": atividade, "value": atividade} for atividade in atividades
            ],
            value=atividades[0],  # Set default value to first activity
        ),
        html.Div(id="bubble-map"),
    ]
)


# Define callback to update bubble map when dropdown value changes
@app.callback(Output("bubble-map", "children"), [Input("activity-dropdown", "value")])
def update_bubble_map(selected_activity):
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
        title=f"Count of {selected_activity.capitalize()} by Brazilian State",
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
    )

    # Return the chart component
    return dcc.Graph(figure=fig)


if __name__ == "__main__":
    app.run_server(debug=True)
