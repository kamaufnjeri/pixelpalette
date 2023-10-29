from app import app, db
from app.forms import EditForm
from app.models import Artwork
from flask import flash, redirect, url_for, render_template
from flask_login import login_required


@app.route("/<int:id>", methods=["GET", "POST"])
@login_required
def edit_artwork(id):
    form = EditForm()

    try:
        artwork = Artwork.query.filter_by(id=id).first()
    except Exception as e:
        flash(f"Error: {str(e)}", category="danger")

    if artwork:
        if form.validate_on_submit():
            try:
                # Update the artwork with the new values
                artwork.title = form.title.data
                artwork.description = form.description.data
                artwork.price = form.price.data

                db.session.commit()
                flash('Artwork updated successfully', category='success')
                return redirect(url_for('user_dashboard', username=artwork.owner.username))
            except Exception as e:
                db.session.rollback()
                flash(f"Error updating artwork: {str(e)}", category="danger")

        # Prepopulate the form fields with the artwork data
        form.title.data = artwork.title
        form.description.data = artwork.description
        form.price.data = artwork.price

    return render_template("edit_artwork.html", form=form, artwork=artwork)
