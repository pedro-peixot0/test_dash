from dash import Dash, dcc, page_container, html
import dash_mantine_components as dmc


def create_dash_application(flask_app):
    dash_app = Dash(
        server=flask_app,
        url_base_pathname="/v1/",
        use_pages=True,
        pages_folder="/Users/pedro.peixoto/test_dash/app/main_dash/pages",
    )

    # Define layout
    dash_app.layout = dmc.MantineProvider(
        html.Div(
            children=[
                html.Div(
                    style={
                        "display": "flex",
                        "justify-content":
                        "center",
                        "background-color": "lightgray"
                    },
                    children=[
                        dcc.Link("Home", href="/v1/home", style={"padding": 10}),
                        dcc.Link("Page1", href="/v1/page1", style={"padding": 10}),
                        dcc.Link("Page2", href="/v1/page2", style={"padding": 10}),
                    ],
                ),
                page_container
            ],
        ),
    )

    return dash_app
