from app import app
from flask import render_template


@app.route("/artworks")
def view_artworks():
    return render_template("artworks.html")


@app.route("/<string:username>/artworks/<int:id>")
def single_artwork(id, username):
    
    return render_template("single_artwork.html")


@app.route("/artists")
def artists_page():
    return render_template("artists.html")


@app.route("/<string:username>/artworks")
def artists_artworks(username):
    return render_template("user_artworks.html", username=username)