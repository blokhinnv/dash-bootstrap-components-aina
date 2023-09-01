import dash_bootstrap_components as dbc
from dash import html
import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html

accordion = html.Div(
    dbc.Accordion(
        [
            dbc.AccordionItem(
                [
                    html.P("This is the content of the first section"),
                    dbc.Button("Click here"),
                ],
                title="Item 1",
                header_id="item1id"
            ),
            dbc.AccordionItem(
                [
                    html.P("This is the content of the second section"),
                    dbc.Button("Don't click me!", color="danger"),
                ],
                title="Item 2",
            ),
            dbc.AccordionItem(
                "This is the content of the third section",
                title="Item 3",
                header_id="item1i234d"
            ),
        ],
    )
)



app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = accordion
if __name__ == '__main__':
    app.run_server(debug=True)