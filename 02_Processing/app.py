import dash
from dash import html
from dash import dcc
#import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from layouts import home_layout, recommendations_layout
from callbacks import register_callbacks


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    dbc.NavbarSimple(
        children=[
            dcc.Link('Populares', href='/', className='nav-link'),
            dcc.Link('Recomendaciones', href='/recommendations', className='nav-link')
        ],
        brand='Movie Recommendation',
        color='primary',
        dark=True,
        className='mb-5'
    ),
    html.Div(id='page-content', className='container')
])

register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)
