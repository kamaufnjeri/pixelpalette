from app import app, db
from app.models import Artwork, PurchaseItem, Exhibit_Artwork
from flask import request, flash
from flask_login import login_required, current_user
from flask import redirect, url_for


@app.route("/delete_artwork/<int:id>", methods=["POST"])
@login_required
def delete_artwork(id):
    artwork = Artwork.query.filter_by(id=id).first()
    if id:
        if request.method == "POST":
            try:
                cart_items = PurchaseItem.query.filter_by(artwork_id=artwork.id).all()
                exhibit_artworks = Exhibit_Artwork.query.filter_by(artwork_id=artwork.id).all()
                for cart_item in cart_items:
                    db.session.delete(cart_item)
                
                for exhibit_artwork in exhibit_artworks:
                    db.session.delete(exhibit_artwork)
                    
                db.session.delete(artwork)
                db.session.commit()
                flash("Artwork successfully deleted", category="success")
                return redirect(url_for('user_dashboard', username=current_user.username))
            except Exception as e:
                db.session.rollback()  # Roll back the transaction on error
                flash(f"Error deleting artwork: {str(e)}", category="danger")
                return redirect(url_for('user_dashboard', username=current_user.username))
            