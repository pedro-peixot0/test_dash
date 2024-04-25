from dash import Dash, get_app
from dash import html, register_page
from dash.dependencies import Input, Output
import dash_mantine_components as dmc

# registers the page to the dash app. The page name is the module name
register_page(__name__)

layout = html.Div(
    children=[
        # password input
        dmc.PasswordInput(
            id="password-input",
            placeholder="Your Password",
            disabled=False
        ),
        # div to display the password
        html.Div(id="password-output")
    ]
)

# creating callback to display the password
app: Dash = get_app()

@app.callback(
    Output("password-output", "children"),
    Input("password-input", "value")
)
def _test_callback(password:str):
    return f"Your password is {password}"
