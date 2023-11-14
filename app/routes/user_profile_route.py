from app import app, bcrypt, db
from flask import request, flash, render_template, redirect, url_for
from app.forms import ProfileForm
from app.models import User
from flask_login import login_required, current_user


"""edit user details"""
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
            category = form.category.data
            user = User.query.filter_by(username=username).first()
            
            if user:
                """check user exists and update their details"""
                user.username = updated_username
                user.first_name = first_name
                user.last_name = last_name
                user.email_address = email_address
                user.category = category
                
                if form.password1.data:
                    """hash the new password to be set"""
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
            """flash any errors user may make while they input info in a form"""
            flash(f"You have the following error: {error_msg}", category='danger')
    form.category.data = current_user.category
    
    return render_template("user_profile.html", form=form)