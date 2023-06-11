from dash.dependencies import Input, Output
from dash import html
import dash_bootstrap_components as dbc
import layouts
import sqlite3
import threading


def register_callbacks(app):
    @app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
    def display_page(pathname):
        if pathname == '/':
            return layouts.home_layout()
        elif pathname == '/recommendations':
            return layouts.recommendations_layout()
        else:
            return '404 - Página no encontrada'
    conn = sqlite3.connect('movies.db')
    

    @app.callback(Output('output-div', 'children'), [Input('gender', 'value'),Input('plat', 'value')])
    def filtrar(gen,plat):
        with threading.Lock(), sqlite3.connect('movies.db') as conn:
            cursor = conn.cursor()
            # Consulta SQL para obtener datos de la tabla
            cursor.execute(f"SELECT * FROM movies WHERE genero LIKE '%{gen}%' AND streaming LIKE '%{plat}%' ORDER BY calificacion DESC LIMIT 10")
            results = cursor.fetchall()

            # Crear la tabla HTML para desplegar los resultados
            table = dbc.Table(
                # Encabezados de columna
                [html.Thead(html.Tr([html.Th(col) for col in ['id','Title','Rating', 'Views','Release Date','Genre', 'Streaming Platforms']]))] +
                # Contenido de la tabla
                [html.Tr([html.Td(col) for col in row]) for row in results],
                bordered=True,
                striped=True,
                hover=True,
                color='primary',
                responsive=True
            )

            return table
        

    conn.close()
