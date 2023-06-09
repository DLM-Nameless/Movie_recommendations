import requests
import json

# Llave de API de The Movie DB
api_key = "a88fba1e1f31a7d6a5069ba558f0b210"

# URL base para la API de The Movie DB
base_url = "https://api.themoviedb.org/3/"

# Endpoint para obtener todas las películas
movies_endpoint = "discover/movie"

# Parámetros para la consulta a la API
params = {
    "api_key": api_key,
    "sort_by": "popularity.desc",
    "language": "es-MX",
    "with_original_language": "en",
    "timezone": "America/Mexico_City",
    "with_watch_monetization_types": "flatrate",
    "page": 1,
    "include_adult": False
}

# Lista vacía para almacenar los datos de las películas
movies_data = []

# Loop para recorrer todas las páginas de resultados
while params["page"] <= 200:
    # Hacer la petición GET a la API
    response = requests.get(base_url + movies_endpoint, params=params)
    # Convertir la respuesta a JSON
    response_json = json.loads(response.content)
    # Obtener los resultados de la consulta
    results = response_json["results"]
    # Si no hay más resultados, salir del loop
    if not results:
        break
    # Loop para procesar los resultados de la página actual
    for result in results:
        # Obtener los datos de la película
        movie_data = {
            "nombre": result["title"],
            "calificacion": result["vote_average"],
            "vistas": result["popularity"],
            "release_date": result.get("release_date", None),
            "streaming": []
        }
        # Obtener los IDs de los géneros de la película
        genre_ids = result['genre_ids']
        # Obtener los nombres de los géneros correspondientes a los IDs de género
        genre_names = []
        for genre_id in genre_ids:
            genre_url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={api_key}'
            genre_response = requests.get(genre_url)
            genre_data = genre_response.json()
            genre_names.append([genre['name'] for genre in genre_data['genres'] if genre['id'] == genre_id][0])
        movie_data['genero'] = genre_names
        # Obtener los datos de transmisión de la película
        streaming_endpoint = f"movie/{result['id']}/watch/providers"
        streaming_params = {
            "api_key": api_key,
            "region": "MX"
        }
        streaming_response = requests.get(base_url + streaming_endpoint, params=streaming_params)
        streaming_response_json = json.loads(streaming_response.content)
        if "results" in streaming_response_json and "MX" in streaming_response_json["results"]:
            results_mx = streaming_response_json["results"]["MX"]
            if "flatrate" in results_mx:
                for provider in results_mx["flatrate"]:
                    movie_data["streaming"].append(provider["provider_name"])
        # Agregar los datos de la película a la lista
        movies_data.append(movie_data)
    # Incrementar el número de página para la siguiente consulta
    params["page"] += 1

# Va a imprimir titulo, genero, calificacion, vistas y fecha de lanzamiento
for movie in movies_data:
    print(movie)

    
# Guardar los datos en un archivo JSON    
movies_json = json.dumps(movies_data)
with open('movies.json', 'w') as file:
    file.write(movies_json)

