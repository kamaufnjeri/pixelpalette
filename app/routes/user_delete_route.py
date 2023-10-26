from app import app, db
from app.models import User
from flask import flash, redirect, url_for, request
from flask_login import login_required


@app.route("/<string:username>/delete_user", methods=["POST"])
@login_required
def delete_user(username):
    user = User.query.filter_by(username=username).first()
    if user:
        if request.method == "POST":
            try:
                db.session.delete(user)
                db.session.commit()
                flash("User successfully deleted", category="success")
                return redirect(url_for('home'))
            except Exception as e:
                db.session.rollback()  # Roll back the transaction on error
                flash(f"Error deleting user: {str(e)}", category="danger")
                return redirect(url_for('home'))
        else:
            flash("Invalid request method", category="danger")
            return redirect(url_for('home'))
    else:
        flash("User not found", category="danger")
        return redirect(url_for('home'))
