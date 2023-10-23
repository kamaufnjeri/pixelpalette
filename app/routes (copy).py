from app import app, db, bcrypt
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from app.models import User, Artwork
from app.methods import Methods
from app.forms import LoginForm, RegistrationForm, ArtworkForm, ProfileForm


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/create_account", methods=["GET", "POST"])
def create_user():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        email_address = form.email_address.data
        category = form.category.data
        password_hash = bcrypt.generate_password_hash(form.password1.data).decode('utf-8')
        new_user = User(
            username=username, first_name=first_name,
            last_name=last_name, email_address=email_address,
            category=category,
            password_hash=password_hash
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        flash(
            f"Success in creating account. You are logged in as {new_user.username}",
            category="success"
        )
        return redirect(url_for('user_dashboard', username=new_user.username))
    if form.errors != {}:
        for error_msg in form.errors.values():
            flash(f"You have the following error! {error_msg}", category='danger')
    return render_template("create_user.html", form=form)


@app.route("/user_login", methods=["GET", "POST"])
def user_login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user_to_log = User.query.filter_by(username=username).first()
        if user_to_log and user_to_log.check_password_correct(password):
            login_user(user_to_log)
            flash(f"You are logged in as {user_to_log.username}", category="success")
            return redirect(url_for("user_dashboard", username=user_to_log.username))
        else:
            flash(f"The username and password are not a match! Please try again", category="danger")

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
    if request.method == "POST" or form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        price = form.price.data
        category = form.category.data
        image = form.image.data

        methods = Methods()
        image_url = methods.image_upload(image)
        user = User.query.filter_by(username=username).first()
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
                flash('Succesfully added artwork', category='success')
                return redirect(url_for('user_dashboard', username=username))
            except Exception:
                flash('Error adding your artwork. Check the information enetered',
                       category="danger"
                )
        else:
            flash("User not found", category="danger")
    else:
        flash('You can upload your artwork here', category='info')

    return render_template('upload_image.html', form=form)


@app.route("/<string:username>/my_profile", methods=["GET", "POST"])
@login_required
def user_profile(username):
    form = ProfileForm()
    if form.validate_on_submit():
        username = form.username.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        email_address = form.email_address.data
        user = User.query.filter_by(username=username).first()
        if user:
            user.username = username
            user.first_name = first_name
            user.last_name = last_name
            user.email_address = email_address
            
            if form.password1.data != "":
                password_hash = bcrypt.generate_password_hash(form.password1.data).decode('utf-8')
                user.password_hash = password_hash
        
            db.session.commit()
            flash(
                f"Success in updating your profile {user.username}",
                category="success"
            )
            return redirect(url_for('user_profile', username=username))
        else:
            flash(f"Error while changing your profile. User not found. Try again",
                  category="danger"
            )
    if form.errors != {}:
        for error_msg in form.errors.values():
            flash(f"You have the following error! {error_msg}", category='danger')
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
                flash(f"Error deleting user: {str(e)}", category="danger")
                return redirect(url_for('home'))
        else:
            flash("Invalid request method", category="danger")
            return redirect(url_for('home'))
    else:
        flash("User not found", category="danger")
        return redirect(url_for('home'))