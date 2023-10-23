from app import app
from app.models import User, Artwork
from flask import jsonify


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"Status": "Page not found"}), 404



@app.route("/api/users", methods=["GET"])
def all_user():
    all_users = User.query.all()
    users = []
    for user1 in all_users:
        user = {}
        user['username'] = user1.username
        user['first_name'] = user1.first_name
        user['last_name'] = user1.last_name
        user['email_address'] = user1.email_address
        user['category'] = user1.category
        users.append(user)
    return jsonify({"Users": users})

@app.route("/api/artworks", methods=["GET"])
def all_artworks():
    all_artworks = Artwork.query.all()
    artworks = []
    for art in all_artworks:
        artwork = {}
        artwork['title'] = art.title
        artwork['owner'] = art.description
        artwork['category'] = art.category
        artwork['url'] = art.artwork_url
        artworks.append(artwork)
    return jsonify({"Artworks": artworks})