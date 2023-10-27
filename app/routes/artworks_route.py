from app import app, db
from flask import render_template, request, flash
from app.methods import Methods
from app.models import ShoppingCart, Artwork, PurchaseItem
from flask_login import current_user

@app.route("/artworks")
def view_artworks():
    return render_template("artworks.html")

@app.route("/<string:username>/artworks/<int:id>", methods=['GET', 'POST'])
def single_artwork(id, username):
    if request.method == 'POST':
        quantity = request.form['quantity']
        if quantity and current_user.is_authenticated:
            try:
                artwork = Artwork.query.get(id)  # Fetch the artwork
                if artwork:



                    shopping_cart = ShoppingCart.query.filter_by(user_id=current_user.id).first()

                    if shopping_cart:
                        methods = Methods()

                        purchase_item = PurchaseItem.query.filter(PurchaseItem.cart_id == shopping_cart.id,
                                                                  PurchaseItem.user_id == current_user.id,
                                                                PurchaseItem.artwork_id == id).first()
                        if purchase_item:
                            purchase_item.quantity = quantity
                            total_amount = methods.total_price(shopping_cart.purchase_items, purchase_item)
                            shopping_cart.total_amount = total_amount + int(quantity) * float(artwork.price)
                            db.session.commit()
                            flash("The artwork is already in the cart, but its quantity was changed", category="info")
                        else:
                            cart_item = PurchaseItem(
                                artwork_id=id, user_id=current_user.id, quantity=quantity,
                                cart_id=shopping_cart.id, artwork=artwork
                            )
                            total_amount = methods.total_price(shopping_cart.purchase_items, purchase_item=cart_item)
                            
                            shopping_cart.total_amount = total_amount + int(quantity) * float(artwork.price)
                            db.session.add(cart_item)
                            db.session.commit()
                            flash('Successfully added item to the cart', category="success")
                    else:
                        flash('No shopping cart', category="danger")
                else:
                    flash("Artwork not found", category="danger")
            except Exception as e:
                db.session.rollback()
                flash(f'Error: {str(e)}', category="danger")
        else:
            flash('Please enter the quantity and ensure you are logged in', category="danger")

    return render_template("single_artwork.html")

@app.route("/artists")
def artists_page():
    return render_template("artists.html")

@app.route("/<string:username>/artworks")
def artists_artworks(username):
    return render_template("user_artworks.html", username=username)
