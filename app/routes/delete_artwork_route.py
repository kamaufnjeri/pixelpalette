from app import app, db
from app.models import Artwork, PurchaseItem, Exhibit_Artwork
from flask import request, flash
from flask_login import login_required, current_user
from flask import redirect, url_for
from datetime import datetime


"""delete an artwork by owner"""
@app.route("/delete_artwork/<int:id>", methods=["POST"])
@login_required
def delete_artwork(id):
    artwork = Artwork.query.filter_by(id=id).first()
    if artwork:
        if request.method == "POST":
            try:
                exhibit = current_user.exhibits
                current_date = datetime.now()
                exhibit_art = Exhibit_Artwork.query.filter_by(artwork_id=artwork.id).first()
                
                if exhibit and exhibit_art and exhibit.end_date > current_date:
                    """check if artwork is in an exhibit"""
                    flash("Cannot delete artwork. Its part of an exhibit.", category="danger")
                    return redirect(url_for('user_dashboard', username=current_user.username))
                else:
                    cart_items = PurchaseItem.query.filter_by(artwork_id=artwork.id).all()
                    exhibit_artworks = Exhibit_Artwork.query.filter_by(artwork_id=artwork.id).all()
                    for cart_item in cart_items:
                        """Delete the artwork from uses cart"""
                        db.session.delete(cart_item)
                    
                    for exhibit_artwork in exhibit_artworks:
                        """Delere from an exhibit an artwork"""
                        db.session.delete(exhibit_artwork)
                        
                    db.session.delete(artwork)
                    db.session.commit()
                    flash("Artwork successfully deleted", category="success")
                    return redirect(url_for('user_dashboard', username=current_user.username))
                    

            except Exception as e:
                """In case of error rollback from inserting to database"""
                db.session.rollback()
                flash(f"Error deleting artwork. Please try again!.", category="danger")
                return redirect(url_for('user_dashboard', username=current_user.username))
            
            return redirect(url_for('user_dashboard', username=current_user.username))
