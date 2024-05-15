import plotly.express as px
from dash_util import dash_util, styles

# setup
util = dash_util
dcc = util.dash.dcc
html = util.dash.html


def create_chart(df, title="Contagem de categorias"):
    # Split values in the 'scope' column and count unique values
    df["categoria"] = df["categoria"].str.split(", ")
    counts = df["categoria"].explode().value_counts()

    # Plot the counts as a horizontal bar plot using Plotly
    fig = px.bar(
        counts,
        x=counts.values,
        y=counts.index,
        orientation="h",
        labels={"categoria": "Categorias", "x": "Contagem"},
        color_continuous_scale="viridis",
    )
    # Add text annotations for count values beside each bar
    fig.update_traces(text=counts.values, textposition="outside")

    # Determine the maximum count value
    max_count = counts.max()

    # Set the x-axis range to show 30% more than the maximum count value
    x_max = max_count * 1.3
    fig.update_xaxes(range=[0, x_max])

    fig.update_layout(
        showlegend=True,
        font=dict(size=14),
    )  # Hide legend
    fig.update_yaxes(categoryorder="total ascending")
    return html.Div(
        children=[html.H3(title, className=styles["h3"]), dcc.Graph(figure=fig)],
        className="w-full",
    )
