from dash import html
import dash_bootstrap_components as dbc
from dash import dcc

import sqlite3
import threading
def populares():
        with threading.Lock(), sqlite3.connect('movies.db') as conn:
            cursor = conn.cursor()
            # Consulta SQL para obtener datos de la tabla
            cursor.execute(f"SELECT * FROM movies ORDER BY vistas DESC LIMIT 10")
            results = cursor.fetchall()

            # Crear la tabla HTML para desplegar los resultados
            table = dbc.Table(
                # Encabezados de columna
                [html.Thead(html.Tr([html.Th(col) for col in ['id','Title','Rating', 'Views','Release Date','Genre', 'Streaming Platforms']]))] +
                # Contenido de la tabla
                [html.Tr([html.Td(col) for col in row]) for row in results],
                bordered=True,
                hover=True,
                striped=True,
                color='primary',
                responsive=True
            )

        return table





genders = ['Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Documentary', 'Drama',
           'Family', 'Fantasy', 'History', 'Horror', 'Music', 'Mystery', 'Romance', 'Science Fiction',
           'TV Movie', 'Thriller', 'War', 'Western']
plats = ['Amazon Prime Video', 'Apple TV Plus', 'Argo', 'Blim', 'BroadwayHD',
         'Cinépolis KLIC', 'Claro video', 'Classix', 'Cultpix', 'DIRECTV GO',
         'Disney Plus', 'DocAlliance Films', 'Filmin Latino', 'GuideDoc',
         'HBO Max', 'Lionsgate Plus', 'MGM Amazon Channel', 'MUBI', 'Netflix',
         'Netflix basic with Ads', 'Paramount Plus', 'Paramount Plus Apple TV Channel ',
         'Paramount+ Amazon Channel', 'Star Plus', 'Starz Play Amazon Channel']

gender = dcc.Dropdown(id='gender',
                options = [{'label':g,'value':g} for g in genders],
                value = 'Action')
plat = dcc.Dropdown(id='plat',
                options = [{'label':p,'value':p} for p in plats],
                value = 'Amazon Prime Video')



def home_layout():
    return html.Div(
        [
            dbc.Row(dbc.Col(html.H1('Populares'), width = 12, style = {'border':'2px MediumPurple','textAlign': 'center'})),
            html.Div(populares())
            
        ]
    )

def recommendations_layout():
    return html.Div(
        [
            html.Div([html.H4('Select Gender'), gender]), #Seleccionar Género
            html.Div([html.H4('Select Platform'), plat]), #Seleccionar Plataforma
            dbc.Row(dbc.Col(html.H2('Recomendaciones'), width = 10, style = {'border':'2px MediumPurple','textAlign': 'center'})),

            html.Div(id='output-div', className='container')
            
        ]
    )