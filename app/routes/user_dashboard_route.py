from app import app
from flask import flash, render_template
from flask_login import login_required
from app.models import User

# User dashboard to show their artworks and their account details
@app.route("/<string:username>/dashboard")
@login_required
def user_dashboard(username):
    user = User.query.filter_by(username=username).first()
<<<<<<< HEAD
    my_general_artworks = []
    my_exhibit_artworks = []
    if user.category == 'artist':
        for artwork in user.owner_artworks:
            if artwork.type == "general_artwork":
                my_general_artworks.append(artwork)
            elif artwork.type == "exhibit_artwork":
                my_exhibit_artworks.append(artwork)
    return render_template("user_dashboard.html", my_exhibit_artworks=my_exhibit_artworks, my_general_artworks=my_general_artworks)
=======
    my_artworks = []
    exhibit = user.exhibits
    try:
        if user.category == 'artist':
            my_artworks = user.owner_artworks
            
    except Exception:
        flash("User does not exist", category="danger")

    return render_template("user_dashboard.html", my_artworks=my_artworks, exhibit=exhibit)
>>>>>>> befe7cc36126c6f4d13da6d29662277def9508b0
