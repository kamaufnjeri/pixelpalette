from app import app, db, bcrypt
from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app.models import User
from app.forms import LoginForm, RegistrationForm


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
        return redirect(url_for('user_dashboard'))
    if form.errors != {}:
        for error_msg in form.errors.values():
            flash(f"You have the following error!{error_msg}", category='danger')
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
            return redirect(url_for("user_dashboard"))
        else:
            flash(f"The username and password are not a match!PLease try again", category="danger")

    return render_template("user_login.html", form=form)

@app.route("/user_logout")
def user_logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/user_dashboard")
@login_required
def user_dashboard():
    return render_template("user_dashboard.html")

