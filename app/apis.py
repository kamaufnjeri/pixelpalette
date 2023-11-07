from flask import jsonify
from app import app
from app.models import Artwork, User


"""Handle page not found error"""
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Page not found"}, 404)


"""handling internal server error"""
@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({"error": "Internal server error"}, 500)


"""api for all artists with artworks"""
@app.route("/api/artists", methods=["GET"])
def all_users():
    try:
        all_users = User.query.all()
        users = []

        for user1 in all_users:
            """check if user is an artist and has artworks"""
            if user1.category == 'artist' and user1.owner_artworks != []:
                user = {
                    "username": user1.username,
                    "first_name": user1.first_name,
                    "last_name": user1.last_name,
                    "category": user1.category,
                }
                users.append(user)

        return jsonify({"Users": users})

    except Exception as e:
        return jsonify({"error": str(e)}, 500)


"""api for all artworks"""
@app.route("/api/artworks", methods=["GET"])
def all_artworks():
    try:
        all_artworks = Artwork.query.all()
        artworks = []
        if all_artworks:
            for art in all_artworks:
                """if an art has an owner and its an general aartwork"""
                if art.owner and art.type == 'general_artwork':
                    artwork = {
                        "title": art.title,
                        "owner": art.owner.username,
                        "category": art.category,
                        "price": art.price,
                        "url": art.artwork_url,
                        "id": art.id
                    }
                else:
                    continue
                artworks.append(artwork)
            return jsonify({"Artworks": artworks})
        else:
            return jsonify({"error": "Artworks not found"}, 404)

    except Exception as e:
        return jsonify({"error": str(e)}, 500)


"""single artwork api"""
@app.route("/api/<string:username>/artworks/<int:id>", methods=["GET"])
def artwork(id, username):

    try:
        artwork = Artwork.query.filter_by(id=id).first()

        if artwork and artwork.owner != None and artwork.type == "general_artwork":
            artwork_json = {
                "title": artwork.title,
                "price": artwork.price,
                "url": artwork.artwork_url,
                "category": artwork.category,
                "description": artwork.description,
                "owner": artwork.owner.username,
                "contact": artwork.owner.email_address
            }
            return jsonify(artwork_json)
        else:
            return jsonify({"error": "Artwork not found"}, 404)

    except Exception as e:
        return jsonify({"error": str(e)}, 500)


"""artworks by an artist api"""
@app.route("/api/<string:username>/artworks", methods=["GET"])
def artist_artworks(username):
    try:
        artist = User.query.filter_by(username=username).first()
        if artist:
            artworks = []
            for artwork in artist.owner_artworks:
                if artwork.owner != None and artwork.type == "general_artwork":
                    owner_artwork = {
                        "id": artwork.id,
                        "name": artwork.title,
                        "category": artwork.category,
                        "price": artwork.price,
                        "description": artwork.description,
                        "url": artwork.artwork_url
                    }
                    artworks.append(owner_artwork)
                else:
                    continue
            return jsonify({"owner_artworks": artworks});
        else:
            return jsonify({"error": "Artist Not found"}, 404)
    except Exception as e:
        return jsonify({"error": str(e)}, 500)