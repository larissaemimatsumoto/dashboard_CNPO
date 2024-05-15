import dash
from dash import Dash

external_scripts = [
    {"src": "https://cdn.tailwindcss.com"},
    {"src": "https://unpkg.com/vue@3/dist/vue.global.js"},
]


class DashUtil:
    def __init__(self):
        self.app = Dash(__name__, external_scripts=external_scripts)
        self.dash = dash


dash_util = DashUtil()

styles = {
    "link": "font-medium text-blue-600 dark:text-blue-500 hover:underline",
    "h1": "text-5xl font-bold",
    "h2": "text-3xl font-bold",
    "h3": "text-2xl font-bold",
}
