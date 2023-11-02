from app import app, db, bcrypt
from flask import render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User, Artwork, ShoppingCart, Exhibit_Artwork, Exhibits
from app.methods import Methods
from datetime import datetime
from app.forms import LoginForm, RegistrationForm, ArtworkForm, ProfileForm


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/create_account", methods=["GET", "POST"])
def create_user():
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            username = form.username.data
            first_name = form.first_name.data
            last_name = form.last_name.data
            email_address = form.email_address.data
            category = form.category.data
            password_hash = bcrypt.generate_password_hash(form.password1.data).decode('utf-8')

            new_user = User(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email_address=email_address,
                category=category,
                password_hash=password_hash
            )
            db.session.add(new_user)
            db.session.commit()

            login_user(new_user)
            flash(f"Success in creating account. You are logged in as {new_user.username}", category="success")
            return redirect(url_for('user_dashboard', username=new_user.username))
        except Exception as e:
            db.session.rollback()  # Roll back the transaction on error
            flash(f"Error creating account: {str(e)}", category="danger")

    if form.errors:
        for error_msg in form.errors.values():
            flash(f"You have the following error: {error_msg}", category='danger')

    return render_template("create_user.html", form=form)


@app.route("/user_login", methods=["GET", "POST"])
def user_login():
    form = LoginForm()
    if form.validate_on_submit():
        try:
            username = form.username.data
            password = form.password.data
            user_to_log = User.query.filter_by(username=username).first()

            if user_to_log and user_to_log.check_password_correct(password):
                login_user(user_to_log)
                flash(f"You are logged in as {user_to_log.username}", category="success")
                return redirect(url_for("user_dashboard", username=user_to_log.username))
            else:
                flash("The username and password are not a match! Please try again", category="danger")
        except Exception as e:
            flash(f"Error during login: {str(e)}", category="danger")

    return render_template("user_login.html", form=form)


@app.route("/user_logout")
def user_logout():
    logout_user()
    flash("You've been logged out", category="success")
    return redirect(url_for('home'))


@app.route("/<string:username>/dashboard")
@login_required
def user_dashboard(username):
    return render_template("user_dashboard.html")


@app.route("/<string:username>/upload_artwork", methods=["GET", "POST"])
@login_required
def upload_artwork(username):
    form = ArtworkForm()
    if form.validate_on_submit() or request.method == 'POST':
        try:
            title = form.title.data
            description = form.description.data
            category = form.category.data
            image = form.image.data
            methods = Methods()
            image_url = methods.image_upload(image)
            user = User.query.filter_by(username=username).first()

            try:
                price = float(form.price.data)

            except Exception:
                flash("Ensure the price is a number/integer", category="danger")


            if Artwork.query.filter_by(title=title).first() is not None:
                flash(
                    "The title name already exists. Artwork title should be unique",
                      category="danger"
                )

            if user:
                try:
                    new_artwork = Artwork(
                        title=title,
                        description=description,
                        price=price,
                        category=category,
                        artwork_url=image_url,
                        owner_id=user.id
                    )
                    db.session.add(new_artwork)
                    db.session.commit()
                    flash('Successfully added artwork', category='success')
                    return redirect(url_for('user_dashboard', username=username))
                except Exception:
                    db.session.rollback()  # Roll back the transaction on error
                    flash(f"Ensure you have filled all the fields correctly", category="danger")
        except Exception as e:
            db.session.rollback()  # Roll back the transaction on error
            flash(f"Error adding artwork: {str(e)}", category="danger")
    else:
        flash('You can upload your artwork here', category='info')

    return render_template('upload_image.html', form=form)


@app.route("/<string:username>/my_profile", methods=["GET", "POST"])
@login_required
def user_profile(username):
    form = ProfileForm()
    if form.validate_on_submit() or request.method == "POST":
        try:
            updated_username = form.username.data
            first_name = form.first_name.data
            last_name = form.last_name.data
            email_address = form.email_address.data
            user = User.query.filter_by(username=username).first()

            if user:
                user.username = updated_username
                user.first_name = first_name
                user.last_name = last_name
                user.email_address = email_address

                if form.password1.data:
                    password_hash = bcrypt.generate_password_hash(form.password1.data).decode('utf-8')
                    user.password_hash = password_hash

                db.session.commit()
                flash(f"Success in updating your profile {user.username}", category="success")
                return redirect(url_for('user_profile', username=user.username))
        except Exception as e:
            db.session.rollback()  # Roll back the transaction on error
            flash(f"Error updating profile: {str(e)}", category="danger")

    if form.errors:
        for error_msg in form.errors.values():
            flash(f"You have the following error: {error_msg}", category='danger')

    return render_template("user_profile.html", form=form)


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


@app.route('/add_to_cart', methods=['POST'])
@login_required # Ensure that user is logged in to add to cart
def add_to_cart():
    data = request.get_json()
    user_id = data['user_id']
    artwork_id = data['artwork_id']
    quantity = data['quantity']

	# Validate data and check if the artwork exists
    artwork = Artwork.query.get(artwork_id)
    if not artwork or quantity < 1:
        return flash("Error: Invalid artwork or quantity", category="danger")

	# check if the artwork is already in the user's cart
    cart_item = ShoppingCart.query.filter_by(user_id=current_user.id, artwork_id=artwork_id).first()
    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = ShoppingCart(user_id=current_user.id, artwork_id=artwork_id, quantity=quantity)
        db.session.add(cart_item)
    db.session.commit()
    return flash("Artwork added to the cart successfully", category="success")



@app.route("/exhibits")
@login_required
def exhibits():
    
    exhibits = Exhibit_Artwork.query.all()
    return render_template("view_exhibit.html", exhibits=exhibits)


@app.route("/add_exhibit", methods=["POST", "GET"])
@login_required
def add_exhibit():
    if request.method == "POST":
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price')
        start_datetime = request.form.get('start_datetime')
        end_date = request.form.get('end_datetime')

        # Create a new exhibit and add it to the database
        exhibit_date = datetime.strptime(start_datetime, '%Y-%m-%dT%H:%M')
        end_date = datetime.strptime(end_date, '%Y-%m-%dT%H:%M')
        exhibit = Exhibits(name=name, start_date=exhibit_date, end_date=end_date)
        db.session.add(exhibit)
        db.session.commit()

        # Redirect to a success page or the exhibit listing page
        flash("Successfully added an exhibition", "success")
        return redirect(url_for('exhibits'))

    # Render the exhibit creation form for GET requests
    return render_template('add_exhibit.html')
