from app import app
from flask import flash, render_template
from flask_login import login_required
from app.models import User

# User dashboard to show their artworks and their account details
@app.route("/<string:username>/dashboard")
@login_required
def user_dashboard(username):
    user = User.query.filter_by(username=username).first()
    my_general_artworks = []
    my_exhibit_artworks = []
    if user.category == 'artist':
        for artwork in user.owner_artworks:
            if artwork.type == "general_artwork":
                my_general_artworks.append(artwork)
            elif artwork.type == "exhibit_artwork":
                my_exhibit_artworks.append(artwork)
    return render_template("user_dashboard.html", my_exhibit_artworks=my_exhibit_artworks, my_general_artworks=my_general_artworks)
