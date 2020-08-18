from flask import Flask, render_template
import tmdb_client

app = Flask(__name__)

@app.route('/')
def homepage():
    movies = tmdb_client.get_movies(12)
    return render_template("homepage.html", movies=movies)

@app.context_processor
def utility_processor():
    def tmdb_image_url(_poster_path, size):
        return tmdb_client.get_poster_url(_poster_path, size)
    return {"tmdb_image_url": tmdb_image_url}