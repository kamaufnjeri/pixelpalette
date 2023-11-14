from flask import redirect, url_for, flash
from app import app
from flask_login import logout_user


@app.route("/user_logout")
def user_logout():
    """logout a user"""
    logout_user()
    flash("You've been logged out", category="success")
    return redirect(url_for('view_artworks'))