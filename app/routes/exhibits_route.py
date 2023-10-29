from app import app, db, bcrypt
from flask import render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User, Artwork, ShoppingCart, Exhibit_Artwork, Exhibits
from app.methods import Methods
from datetime import datetime
from app.forms import LoginForm, RegistrationForm, ArtworkForm, ProfileForm


@app.route("/exhibits")
def exhibits():
    exhibits = Exhibits.query.all()
    return render_template("exhibits.html", exhibits=exhibits)


@app.route("/exhibits/<int:id>")
def view_exhibits(id):
    exhibit = Exhibits.query.filter_by(id=id).first()
    print(exhibit)
    for exhibit_artworks in exhibit.exhibit_artworks:
        print(exhibit_artworks.artwork.artwork_url)
    # exhibits = Exhibit_Artwork.query.all()
    return render_template("view_exhibit.html", exhibit=exhibit)


@app.route("/add_exhibit", methods=["POST", "GET"])
@login_required
def add_exhibit():

    if request.method == "POST":
        name = request.form.get('name')
        description = request.form.get('description')
        start_datetime = request.form.get('start_datetime')
        end_date = request.form.get('end_datetime')

        # Create a new exhibit and add it to the database
        try:
            exhibit_date = datetime.strptime(start_datetime, '%Y-%m-%dT%H:%M')
            end_date = datetime.strptime(end_date, '%Y-%m-%dT%H:%M')
            exhibit = Exhibits(name=name, description=description, start_date=exhibit_date, end_date=end_date, user_id=current_user.id)
            db.session.add(exhibit)
            db.session.commit()

            # Redirect to a success page or the exhibit listing page
            flash("Successfully added an exhibition", category="success")
            return redirect(url_for('exhibits'))

        except Exception as e:
            db.session.rollback()
            flash(f"error: {str(e)}", category="danger")
        
    
    else:
        flash("Request method invalid", category="danger")

    # Render the exhibit creation form for GET requests
    return render_template('add_exhibit.html')


@app.route("/add_artwork_to_exhibit/<int:id>", methods=["POST", "GET"])
@login_required
def add_artwork_to_exhibit(id):
    if id:
        artwork = Artwork.query.filter_by(id=id).first()
        if artwork:
            try:
                exhibit = current_user.exhibits
                if Exhibit_Artwork.query.filter(
                    Exhibit_Artwork.user_id == current_user.id, 
                    Exhibit_Artwork.artwork_id == id,
                    Exhibit_Artwork.exhibit_id == exhibit.id
                ).first() in exhibit.exhibit_artworks:
                    flash("already added to exhibit", category='danger')
                
                else:
                    exhibit_artwork = Exhibit_Artwork(user_id=current_user.id, artwork_id=id, exhibit_id=exhibit.id, artwork=artwork)
                    db.session.add(exhibit_artwork)
                    db.session.commit()

                    flash("Succesfully added artwork to exhibit", category="success")
                return redirect(url_for('user_dashboard', username=current_user.username))

            except Exception as e:
                db.session.rollback()
                flash(f"error: {str(e)}", category="danger")
                return redirect(url_for('user_dashboard', username=current_user.username))