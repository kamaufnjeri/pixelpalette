from app import app
from flask import flash, render_template
from flask_login import login_required
from app.models import User


@app.route("/<string:username>/dashboard")
@login_required
def user_dashboard(username):
    user = User.query.filter_by(username=username).first()
    my_artworks = []
    try:
        if user.category == 'artist':
            my_artworks = user.owner_artworks
            
    except Exception:
        flash("User does not exist", category="danger")

    return render_template("user_dashboard.html", my_artworks=my_artworks)
