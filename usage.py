import modelviewer
from dash import Dash, callback, html, Input, Output

app = Dash(__name__)

app.layout = html.Div([
    modelviewer.Modelviewer(
        id='input',
        src='assets/M08.glb',
        alt="A rock",
        exposure="0.008",
        style={"width": "100%", "height": "100%"},
    ),
    html.Div(id='output')
],
    style={"position": "absolute", "top": "0px", "left": "0px",
           "width": "100%", "height": "100%", "background-color": "slate"},
)


# @callback(Output('output', 'children'), Input('input', 'value'))
# def display_output(value):
#     return 'You have entered {}'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)