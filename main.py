from flask import Flask, render_template, request
import tmdb_client
import random
from waitress import serve

app = Flask(__name__)

@app.route('/')
def homepage():
    number = random.randint(8,50)
    list = ["popular", "top_rated", "now_playing", "latest", "upcoming"]
    #list = ["popular", "now_playing"]
    selected_list = request.args.get('list_name', "popular")
    if selected_list in list:
        movies = tmdb_client.get_movies(number, list_name=selected_list)
    else:
        movies = tmdb_client.get_movies(number, list_name="popular")
    return render_template("homepage.html", movies=movies, selected_list=selected_list, list=list)

@app.context_processor
def utility_processor():
    def tmdb_image_url(_poster_path, size):
        return tmdb_client.get_poster_url(_poster_path, size)
    return {"tmdb_image_url": tmdb_image_url}

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    number = 6
    movie = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_casts(movie_id, number)
    images = tmdb_client.get_single_movie_image(movie_id)
    rand_image = random.choice(images)
    return render_template("movie_details.html", movie=movie, cast=cast, rand_image = rand_image)

@app.route("/search")
def search(search_query):
    searching = request.args.get('search_query')
    results = tmdb_client.search_movie(search_query = searching)
    return render_template("search.html", results=results, searching = searching) 


if __name__ == "__main__":
serve(app, host='0.0.0.0', port=80)
