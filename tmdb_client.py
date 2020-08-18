import requests


def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjNmJjYzM4ODI4Y2UwN2ZjNjQyMGVlZjQ2MmQwOTIxYSIsInN1YiI6IjVmMzUwYWIzMTExZGExMDAzNTY0ZDAyZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.23GKKLcjf9Uewp6Z7d3imx7RuE9r3y6FnP_O2Lq0yXo"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_movies(how_many):
    data = get_popular_movies()
    return data["results"][:how_many]


def get_poster_url(_poster_path, size='w342'):
    base_url = "http://image.tmdb.org/t/p/"
    url = f"{base_url}{size}{_poster_path}"
    return url



