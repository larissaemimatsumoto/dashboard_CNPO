import pandas as pd
from dash_util import dash_util, styles

# fig charts
import charts.atividades_x_uf as atv_x_uf

import charts.atividades_x_pais as atv_x_pais
import charts.categorias_count as cat_count
import charts.categorias_x_uf_heatmap as cat_x_uf_heat
import charts.categorias_x_pais_heatmap as cat_x_pais_heat
import charts.mapa as mapa

util = dash_util
app = util.app
html = util.dash.html
dados_br = pd.read_csv("./dados_br.csv")
dados_exterior = pd.read_csv("./dados_exterior.csv")


app.layout = html.Div(
    className="p-7 space-y-7",
    children=[
        # titulo
        html.Div(
            children=[
                html.H1(
                    "Análise do Cadastro Nacional de Produtores Orgânicos (CNPO)",
                    className=styles["h1"],
                ),
                html.Div(
                    children=[
                        html.Span("Fonte: "),
                        html.A(
                            "https://www.gov.br/agricultura/pt-br/assuntos/sustentabilidade/organicos/cadastro-nacional-produtores-organicos",
                            href="https://www.gov.br/agricultura/pt-br/assuntos/sustentabilidade/organicos/cadastro-nacional-produtores-organicos",
                            className=styles["link"],
                        ),
                    ]
                ),
            ]
        ),
        html.H2("Categorias de Produção Orgânica no Brasil", className=styles["h2"]),
        html.Div(
            className="flex items-start justify-around",
            children=[
                cat_count.create_chart(dados_br, "Contagem de categorias do Brasil"),
                cat_x_uf_heat.chart,
            ],
        ),
        atv_x_uf.create_chart(dados_br, "Variedade de Produtos por UF"),
        mapa.layout,
        html.H2("Categorias de Produção Orgânica no Exterior", className=styles["h2"]),
        html.Div(
            className="flex items-start justify-around",
            children=[
                cat_count.create_chart(
                    dados_exterior, "Contagem de categorias por País"
                ),
                cat_x_pais_heat.chart,
            ],
        ),
        atv_x_pais.create_chart(dados_exterior, "Variedade de Produtos por País"),
    ],
)

if __name__ == "__main__":
    app.run(debug=True, port=8080)
