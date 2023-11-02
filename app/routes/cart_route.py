from app import app, db
from flask_login import login_required, current_user
from app.models import ShoppingCart, PurchaseItem
from flask import render_template, flash, redirect, url_for, request
from app.methods import Methods

@app.route('/<string:username>/cart/<int:id>', methods=['GET', 'POST'])
@login_required
def cart(username, id):
    # Check if the current user is authenticated
    if current_user.is_authenticated:
        cart = ShoppingCart.query.filter_by(user_id=current_user.id).first()
        if cart:

            return render_template('cart.html', cart=cart)
        else:
            # Handle the case where the user doesn't have a cart
            flash("Cart not found", category="danger")
    else:
        # Handle the case where the user is not authenticated
        flash("Please log in to access the favorites cart", category="danger")

    # Handle redirection or other actions for unauthenticated users
    return redirect(url_for('user_login'))

@app.route('/remove_item_from_cart/<int:id>', methods=['GET', 'POST'])
@login_required
def remove_item_from_cart(id):
    if current_user:
        shopping_cart = current_user.cart

        if request.method == "POST":
            delete_item = PurchaseItem.query.filter(
				PurchaseItem.user_id == current_user.id,
				PurchaseItem.cart_id == current_user.cart.id,
				PurchaseItem.id == id
			).first()

            if delete_item:
                shopping_cart.total_amount -= float(delete_item.artwork.price) * delete_item.quantity
                db.session.delete(delete_item)
                db.session.commit()
                flash("Item succesfully removed from cart", category="success")
                return redirect(url_for("cart", username=current_user.username, id=shopping_cart.id))

            else:
                flash("Item not in cart", category="danger")
                return redirect(url_for("cart", username=current_user.username, id=shopping_cart.id))

        else:
            flash("Request method not allowed", category="danger")
            return redirect(url_for("cart", username=current_user.username, id=shopping_cart.id))



@app.route('/update_cart_item_quantity/<int:id>', methods=['GET', 'POST'])
@login_required
def update_cart_quantity(id):
    if current_user:
        if request.method == "POST":
            shopping_cart = current_user.cart
            update_quantity_item = PurchaseItem.query.filter(
                PurchaseItem.user_id == current_user.id,
				PurchaseItem.cart_id == current_user.cart.id,
				PurchaseItem.id == id
			).first()

            if update_quantity_item:
                quantity = request.form.get("quantity")
                update_quantity_item.quantity = quantity
                methods = Methods()
                total_amount = methods.total_price(shopping_cart.purchase_items, update_quantity_item)
                shopping_cart.total_amount = total_amount + int(quantity) * float(update_quantity_item.artwork.price)
                db.session.commit()
                flash("Quantity changed", category="success")
                return redirect(url_for("cart", username=current_user.username, id=shopping_cart.id))
            else:
                flash("Item not in cart", category="danger")
                return redirect(url_for("cart", username=current_user.username, id=shopping_cart.id))

        else:
            flash("Request method not allowed", category="danger")
            return redirect(url_for("cart", username=current_user.username, id=shopping_cart.id))
