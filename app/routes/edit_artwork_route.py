from app import app, db
from app.forms import EditForm
from app.models import Artwork, Exhibit_Artwork
from flask import flash, redirect, url_for, render_template
from flask_login import login_required, current_user
from datetime import datetime


"""Change details eg title of an artwork"""
@app.route("/<int:id>", methods=["GET", "POST"])
@login_required
def edit_artwork(id):
    form = EditForm()
    try:
        artwork = Artwork.query.filter_by(id=id).first()
    except Exception as e:
        flash(f"Error: Artwork not available", category="danger")

    if artwork:
        if form.validate_on_submit():
            try:
                """ Update the artwork with the new values"""  
                try:
                    """check price is an integer or float"""
                    price = float(form.price.data)
                except Exception:
                    flash("Price should be an number", category="danger")
                artwork.title = form.title.data
                artwork.description = form.description.data
                artwork.category = form.category.data

                exhibit = current_user.exhibits
                current_date = datetime.now()
                exhibit_art = Exhibit_Artwork.query.filter_by(artwork_id=artwork.id).first()
                if exhibit and (exhibit.start_date <= current_date and exhibit.end_date >= current_date)  and exhibit_art:
                    """if user has an exhibit and if it has began"""
                    flash("Can't change type of artwork if exhibit is ongoing", category="danger")
                else:
                    artwork.type = form.type.data
                artwork.price = price
                db.session.commit()
                flash('Artwork updated successfully', category='success')
                return redirect(url_for('user_dashboard', username=artwork.owner.username))
            except Exception as e:
                db.session.rollback()
                flash(f"Error updating artwork: {str(e)}", category="danger")

        """set default for form fields with the artwork data"""
        form.title.data = artwork.title
        form.description.data = artwork.description
        form.price.data = artwork.price
        form.category.data = artwork.category
        form.type.data = artwork.type

    return render_template("edit_artwork.html", form=form, artwork=artwork)
