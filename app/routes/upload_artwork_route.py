from app import app, db
from flask import request, flash, render_template, redirect, url_for
from flask_login import login_required
from app.methods import Methods
from app.models import User, Artwork
from app.forms import ArtworkForm


"""uploading an artwork"""
@app.route("/<string:username>/upload_artwork", methods=["GET", "POST"])
@login_required
def upload_artwork(username):
    form = ArtworkForm() #form for uploading artwork
    if form.validate_on_submit() or request.method == 'POST':
        """check form submition"""
        try:
            title = form.title.data
            description = form.description.data
            category = form.category.data
            image = form.image.data
            type = form.type.data
            methods = Methods()
            image_url = methods.image_upload(image) #method to add image of artwork to cloudinary
            user = User.query.filter_by(username=username).first()

            try:
                """ensure price is a float or integer"""
                price = float(form.price.data)

            except Exception:
                flash("Ensure the price is a number", category="danger")


            if Artwork.query.filter_by(title=title).first() is not None:
                """ensure the name of artwork is unique"""
                flash("The title name already exists. Artwork title should be unique", category="danger")

            if user:
                """Start a database transaction using a context manager"""
                with db.session.begin_nested():
                    new_artwork = Artwork(
                        title=title,
                        description=description,
                        price=price,
                        type=type,
                        category=category,
                        artwork_url=image_url,
                        owner_id=user.id
                    )
                    db.session.add(new_artwork)

                """ Commit the transaction"""
                db.session.commit()

                flash('Successfully added artwork', category='success')
                return redirect(url_for('user_dashboard', username=username))

        except Exception as e:
            db.session.rollback()  # Roll back the transaction on error
            flash(f"Error adding artwork: {str(e)}", category="danger")


    return render_template('upload_image.html', form=form)