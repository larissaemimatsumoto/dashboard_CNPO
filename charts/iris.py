from dash import Dash, dcc, html, Input, Output
import plotly.express as px

colorscales = px.colors.named_colorscales()

app = Dash(__name__)


app.layout = html.Div(
    [
        html.H4("Interactive Plotly Express color scale selection"),
        html.P("Color Scale"),
        dcc.Dropdown(id="dropdown", options=colorscales, value="viridis"),
        dcc.Graph(id="graph"),
    ]
)


@app.callback(Output("graph", "figure"), Input("dropdown", "value"))
def change_colorscale(scale):
    df = px.data.iris()  # replace with your own data source
    fig = px.scatter(
        df,
        x="sepal_width",
        y="sepal_length",
        color="sepal_length",
        color_continuous_scale=scale,
    )
    return fig


app.run_server(debug=True)
