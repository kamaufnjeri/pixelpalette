from app import app, bcrypt, db
from app.forms import RegistrationForm
from app.models import User, ShoppingCart
from flask import flash, render_template, redirect, url_for
from flask_login import login_user


@app.route("/create_account", methods=["GET", "POST"])
def create_user():
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            username = form.username.data
            if " " in username:
                flash("Username needs to be a single word without spaces", category="danger")
            else:

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
                cart = ShoppingCart(user_id=new_user.id, total_amount=0)
                db.session.add(cart)
                db.session.commit()
                flash(f"Success in creating account. You are logged in as {new_user.username}", category="success")
                return redirect(url_for('user_dashboard', username=new_user.username))
        except Exception as e:
            db.session.rollback()  # Roll back the transaction on error
            flash(f"Error creating account: {str(e)}", category="danger")

    if form.errors:
        for error_msg in form.errors.values():
            flash(f"You have the following error: {error_msg}", category='danger')

    return render_template("create_user.html", form=form)

