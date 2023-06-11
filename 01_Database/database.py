import sqlite3
import json
import time

conn = sqlite3.connect('movies.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS movies
             (id INTEGER PRIMARY KEY,
             nombre TEXT,
             calificacion FLOAT,
             vistas FLOAT,
             release_date TEXT,
             genero TEXT,
             streaming TEXT)''')
while True:
    # Obtener los datos de las películas del archivo JSON
  with open('movies.json', 'r') as f:
    movies_data = json.load(f)
    
  # Insertar los datos de las películas en la tabla de la base de datos
   for movie in movies_data:
      c.execute("INSERT INTO movies (nombre, calificacion, vistas, release_date, genero, streaming) VALUES (?, ?, ?, ?, ?, ?)",
              (movie["nombre"], movie["calificacion"], movie["vistas"], movie["release_date"], ", ".join(movie["genero"]), ", ".join(movie["streaming"])))
    
    # Guardar los cambios en la base de datos
  conn.commit()
    
    # Esperar 1 minuto antes de volver a leer el archivo JSON
    time.sleep(60)
conn.close()
