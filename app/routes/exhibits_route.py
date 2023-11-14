from app import app, db
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.models import Artwork, Exhibit_Artwork, Exhibits
from datetime import datetime


"""All exhibits with artworks"""
@app.route("/exhibits")
def exhibits():
    exhibits = Exhibits.query.all()
    current_date = datetime.now()
    current_exhibits = []
    for exhibit in exhibits:
        if exhibit.end_date > current_date and exhibit.exhibit_artworks != []:
            """append only those exhibits with artworks and have not yet reached the end date"""
            current_exhibits.append(exhibit)
    return render_template("exhibits.html", current_exhibits=current_exhibits)


"""Route to see exhibits artworks"""
@app.route("/exhibits/<int:id>")
def view_exhibits(id):
    exhibit = Exhibits.query.filter_by(id=id).first()
    """"Within the ongoing period"""
    current_date = datetime.now()
    time_frame = exhibit.start_date <= current_date <= exhibit.end_date
    return render_template("view_exhibit.html", exhibit=exhibit, time_frame=time_frame)


"""Create or edit an exhibit route"""
@app.route("/<string:username>/add_exhibit", methods=["POST", "GET"])
@login_required
def add_exhibit(username):
    if request.method == "POST":
        name = request.form.get('name')
        description = request.form.get('description')
        start_datetime = request.form.get('start_datetime')
        end_date = request.form.get('end_datetime')

        current_date = datetime.now()
        existing_exhibit = current_user.exhibits

        if not existing_exhibit:
            """" User doesn't have an existing exhibition, so allow them to create a new one."""
            try:
                exhibit_date = datetime.strptime(start_datetime, '%Y-%m-%dT%H:%M')
                end_date = datetime.strptime(end_date, '%Y-%m-%dT%H:%M')

                exhibit = Exhibits(name=name, description=description, start_date=exhibit_date, end_date=end_date, user_id=current_user.id)
                db.session.add(exhibit)
                db.session.commit()

                flash("Successfully added an exhibition", category="success")
                return redirect(url_for('user_dashboard', username=current_user.username))

            except Exception as e:
                """incase of an error"""
                db.session.rollback()
                flash(f"Error creating exhibit: Try again!", category="danger")
                return redirect(url_for('add_exhibit', username=username))
        else:
            """User has an existing exhibition, check if it's before the end date."""
            if existing_exhibit.end_date > current_date and existing_exhibit.exhibit_artworks != []:
                flash("You already have an ongoing exhibition. You can create an exhibit after the current one ends.", category="danger")
                return redirect(url_for('user_dashboard', username=username))
            else:
                """modify the existing exhibition."""
                try:
                    exhibit_date = datetime.strptime(start_datetime, '%Y-%m-%dT%H:%M')
                    end_date = datetime.strptime(end_date, '%Y-%m-%dT%H:%M')

                    existing_exhibit.name = name
                    existing_exhibit.description = description
                    existing_exhibit.start_date = exhibit_date
                    existing_exhibit.end_date = end_date
                    for exhibit_artwork in existing_exhibit.exhibit_artworks:
                        """if modifying delete all artworks in the previous exhibit"""
                        db.session.delete(exhibit_artwork)

                    db.session.commit()

                    flash("Successfully created a new exhibit", category="success")
                    return redirect(url_for('user_dashboard', username=current_user.username))

                except Exception as e:
                    db.session.rollback()
                    flash(f"Error creating exhibit: Try again!", category="danger")
                    return redirect(url_for('add_exhibit', username=username))
                
    return render_template('add_exhibit.html')


"""adding an artwork to an exhibit"""
@app.route("/add_artwork_to_exhibit/<int:id>", methods=["POST", "GET"])
@login_required
def add_artwork_to_exhibit(id):
    if id:
        artwork = Artwork.query.filter_by(id=id).first()
        if artwork:
            """check artwork exists"""
            try:
                exhibit = current_user.exhibits
                if exhibit:
                    """check user has an exhibit"""
                    current_date = datetime.now()
                    if current_date < exhibit.start_date:
                        """check the exhibit is yet to start"""
                        if Exhibit_Artwork.query.filter(
                            Exhibit_Artwork.user_id == current_user.id, 
                            Exhibit_Artwork.artwork_id == id,
                            Exhibit_Artwork.exhibit_id == exhibit.id
                        ).first() in exhibit.exhibit_artworks:
                            """check if artwork is already in the exhibit"""
                            flash("Artwork already added to exhibit", category='danger')
                        
                        else:
                            """add artwork to exhibit if it is yet to start"""
                            exhibit_artwork = Exhibit_Artwork(user_id=current_user.id, artwork_id=id, exhibit_id=exhibit.id, artwork=artwork)
                            db.session.add(exhibit_artwork)
                            db.session.commit()

                            flash("Succesfully added artwork to exhibit", category="success")
                        return redirect(url_for('user_dashboard', username=current_user.username))
                    
                    elif current_date >= exhibit.start_date and current_date <= exhibit.end_date:
                        """check exhibit if ongoing"""
                        flash("Exhibition is ongoing", category="danger")
                        return redirect(url_for('user_dashboard', username=current_user.username))
                    else:
                        """check if the exhibit is over"""
                        flash("You need to create a new exhibit", category="danger")
                        return redirect(url_for('add_exhibit', username=current_user.username))
                    
                else:
                    """if the exhibit is not created"""
                    flash("You need to create an exhibit", category="danger")
                    return redirect(url_for('add_exhibit', username=current_user.username))

            except Exception as e:
                """incase of an error"""
                db.session.rollback()
                flash(f"Error: {str(e)}", category="danger")
                return redirect(url_for('user_dashboard', username=current_user.username))


"""removing an artwork from an exhibit"""
@app.route("/remove_from_exhibit/<int:artwork_id>", methods=["POST", "GET"])
@login_required
def remove_from_exhibit(artwork_id):
    if request.method == "POST":
        artwork_to_remove = Exhibit_Artwork.query.filter_by(artwork_id=artwork_id).first()
        exhibit = current_user.exhibits
        if exhibit and artwork_to_remove:
            """check user has an exhibit and artwork is in the exhibit"""
            current_date = datetime.now()
            try:
                if current_date < exhibit.start_date:
                    """only remove the artwork if exhibit is yet to start"""
                    db.session.delete(artwork_to_remove)
                    db.session.commit()
                    flash("Successfully removed artwork from exhibit", category="success")
                    return redirect(url_for('user_dashboard', username=current_user.username))
                
                elif current_date >= exhibit.start_date and current_date <= exhibit.end_date:
                        """don't remove if the current date is within the start and end date of exhibit"""
                        flash("Exhibition is ongoing", category="danger")
                        return redirect(url_for('user_dashboard', username=current_user.username))
                    
                else:
                    """if the exhibit is over"""
                    flash("No exhibition ongoing", category="danger")
                    return redirect(url_for('user_dashboard', username=current_user.username))
            except Exception as e:
                """incase of an error"""
                flash(f"Error: {str(e)}", category="success")
                return redirect(url_for('user_dashboard', username=current_user.username))
        else:
            """incase artwork is not in exhibiyt"""
            flash("Artwork not in exhibit", category="danger")
            return redirect(url_for('user_dashboard', username=current_user.username))


"""Deleting an exhibit"""
@app.route('/delete_exhibit/<int:id>', methods=["GET", 'POST'])
@login_required
def delete_exhibit(id):
    exhibit = Exhibits.query.filter_by(id=id).first()
    if exhibit:
        """check if exhibit exists"""
        current_date = datetime.now()
        if current_date >= exhibit.start_date and current_date <= exhibit.end_date and exhibit.exhibit_artworks != []:
            """if exhibit is ongoing and has artworks don't delete"""
            flash("Exhibition is ongoing", category="danger")
            return redirect(url_for('user_dashboard', username=current_user.username))

        if exhibit.exhibit_artworks != []:
            """delete all artworks in an exhibit"""
            for exhibit_artwork in exhibit.exhibit_artworks:
                db.session.delete(exhibit_artwork)
        db.session.delete(exhibit) #delete exhibit
        db.session.commit()
        flash("Successfully deleted exhibit", category="success")
        return redirect(url_for('user_dashboard', username=current_user.username))
    else:
        """incase the exhibit does not exist"""
        flash("No exhibit", category="danger")
        return redirect(url_for('user_dashboard', username=current_user.username))
    

"""Edit an exhibit"""
@app.route("/<string:username>/edit_exhibit/<int:exhibit_id>", methods=["POST", "GET"])
def edit_exhibit(username, exhibit_id):
    exhibit = Exhibits.query.filter_by(id=exhibit_id).first()
    current_date = datetime.now()
    if exhibit:
        """check exibit exists"""
        if request.method == "POST":
            name = request.form.get('name')
            description = request.form.get('description')
            start_datetime = request.form.get('start_datetime')
            end_date = request.form.get('end_datetime')

            """check if the exhibit has started"""
            if  current_date >= exhibit.start_date and current_date <= exhibit.end_date:
                flash("Exhibit is ongoing", category="danger")
                return redirect(url_for('user_dashboard', username=username))
            else:
                """modify the existing exhibition."""
                try:
                    exhibit_date = datetime.strptime(start_datetime, '%Y-%m-%dT%H:%M')
                    end_date = datetime.strptime(end_date, '%Y-%m-%dT%H:%M')

                    exhibit.name = name
                    exhibit.description = description
                    exhibit.start_date = exhibit_date
                    exhibit.end_date = end_date
                    
                    db.session.commit()

                    flash("Successfully updated exhibit", category="success")
                    return redirect(url_for('user_dashboard', username=current_user.username))

                except Exception as e:
                    db.session.rollback()
                    flash(f"Error updating exhibit: Try again!", category="danger")
                    return redirect(url_for('add_exhibit', username=username))

    return render_template("edit_exhibit.html", exhibit=exhibit)
