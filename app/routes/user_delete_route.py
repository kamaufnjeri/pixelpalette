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
                exhibit = user.exhibits
                cart = user.cart
                # delete items for user in cart
                if cart:
                    for artwork in cart.purchase_items:
                        db.session.delete(artwork)
                    db.session.delete(cart)
                # delete artworks in exhibit for the user
                if exhibit:
                    for artwork in exhibit.exhibit_artworks:
                        db.session.delete(artwork)
                    db.session.delete(exhibit)

                # delete artworks by user
                if user.owner_artworks:
                    for artwork in user.owner_artworks:
                        db.session.delete(artwork)

                #delete users artworks

                db.session.delete(user)
                db.session.commit()
                flash("User successfully deleted", category="success")
                return redirect(url_for('view_artworks'))
            except Exception as e:
                db.session.rollback()  # Roll back the transaction on error
                flash(f"Error deleting user: {str(e)}", category="danger")
                return redirect(url_for('view_artworks'))
        else:
            flash("Invalid request method", category="danger")
            return redirect(url_for('view_artworks'))
    else:
        flash("User not found", category="danger")
        return redirect(url_for('view_artworks'))
