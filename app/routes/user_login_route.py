from app import app
from app.models import User
from app.forms import LoginForm
from flask import flash, redirect, url_for, render_template
from flask_login import login_user


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