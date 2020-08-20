import requests

my_api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjNmJjYzM4ODI4Y2UwN2ZjNjQyMGVlZjQ2MmQwOTIxYSIsInN1YiI6IjVmMzUwYWIzMTExZGExMDAzNTY0ZDAyZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.23GKKLcjf9Uewp6Z7d3imx7RuE9r3y6FnP_O2Lq0yXo"



def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    headers = {
        "Authorization": f"Bearer {my_api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_movies_list(list_name):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_name}"
    headers = {
        "Authorization": f"Bearer {my_api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()



def get_movies(how_many, list_name):
    data = get_movies_list(list_name)
    return data["results"][:how_many]


def get_poster_url(_poster_path, size='w342'):
    base_url = "http://image.tmdb.org/t/p/"
    url = f"{base_url}{size}{_poster_path}"
    return url

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {my_api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_single_movie_image(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {my_api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()['backdrops']


def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {my_api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()['cast']

def get_casts(movie_id, how_many):
    data = get_single_movie_cast(movie_id)
    return data[:how_many]