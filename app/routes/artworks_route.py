from app import app, db
from flask import render_template, request, flash, redirect, url_for
from app.methods import Methods
from app.models import ShoppingCart, Artwork, PurchaseItem, Exhibit_Artwork
from flask_login import current_user, login_required
from datetime import datetime


"""Home route with all the general artworks"""
@app.route("/artworks")
@app.route("/")
@app.route("/home")
def view_artworks():
    return render_template("artworks.html")


"""route for each individual artwork"""
@app.route("/<string:username>/artworks/<int:id>", methods=['GET', 'POST'])
def single_artwork(id, username):
    """added the functionality of adding to favorites cat"""
    if request.method == 'POST':
        quantity = request.form['quantity']
        if quantity == '':
            """If quantity is emty set to one"""
            quantity = 1
        if current_user.is_authenticated:
            """check user is authenticated"""
            try:
                artwork = Artwork.query.get(id)
                if artwork:
                    """check artwork exists"""
                    shopping_cart = ShoppingCart.query.filter_by(user_id=current_user.id).first()
                    if shopping_cart:
                        """check if shopping cart exists"""
                        methods = Methods()
                        purchase_item = PurchaseItem.query.filter(
                            PurchaseItem.cart_id == shopping_cart.id,
                            PurchaseItem.user_id == current_user.id,
                            PurchaseItem.artwork_id == id
                        ).first()
                        if purchase_item:
                            """check if purchase item exists to change total amount based on new quantity"""
                            purchase_item.quantity = quantity
                            total_amount = methods.total_price(shopping_cart.purchase_items, purchase_item)
                            shopping_cart.total_amount = total_amount + int(quantity) * float(artwork.price)
                            db.session.commit()
                            flash("The artwork is already in the cart, but its quantity was updated", category="info")
                            return redirect(url_for('view_artworks'))
                        else:
                            """create new purchase item and calculate new total amount"""
                            cart_item = PurchaseItem(
                                artwork_id=id, user_id=current_user.id, quantity=quantity,
                                cart_id=shopping_cart.id, artwork=artwork
                            )
                            total_amount = methods.total_price(shopping_cart.purchase_items, purchase_item=cart_item)
                            
                            shopping_cart.total_amount = total_amount + int(quantity) * float(artwork.price)
                            db.session.add(cart_item)
                            db.session.commit()
                            flash('Successfully added item to favorite artworks cart', category="success")
                            return redirect(url_for('view_artworks'))
                    else:
                        flash('No shopping cart', category="danger")
                        return redirect(url_for('view_artworks'))
                else:
                    flash("Artwork not found", category="danger")
                    return redirect(url_for('view_artworks')) 
            except Exception as e:
                """Roll back incase of an Exception"""
                db.session.rollback()
                flash(f'Error: Try again!', category="danger")
        else:
            flash('Please ensure you are logged in', category="danger")
            return redirect(url_for('user_login'))


    return render_template("single_artwork.html")


"""All artists page"""
@app.route("/artists")
def artists_page():
   return render_template("artists.html")


"""all artist artworks page"""
@app.route("/<string:username>/artworks")
def artists_artworks(username):
    return render_template("user_artworks.html", username=username)


"""search an artwork by title/name"""
@app.route("/search", methods=["POST", "GET"])
def search_function():
    if request.method == "POST":
        search_word = request.form.get('search-word')
        if search_word:
            """if search word is entered"""
            search_term = f"%{search_word}%"
            artworks_search = Artwork.query.filter(Artwork.title.ilike(search_term), Artwork.type == "general_artwork").all()
            if artworks_search:
                """search artwork by the title and ensure its a general artwork"""
                flash("Artworks matching the search word found", category="success")
                return render_template("search.html", artworks_search=artworks_search)
            else:
                flash("No artworks match the search word", category="danger")
                return render_template("search.html")
        else:
            flash("Please enter a search term", category="danger")
            return render_template("search.html")

    return render_template("search.html")

"""change an artwork from an exhibit artwork to a general artwork"""
@app.route("/add_to_general_artworks/<int:id>", methods=["POST"])
@login_required
def add_to_general_artworks(id):
    if request.method == "POST":
        artwork = Artwork.query.filter_by(id=id).first()
        exhibit = current_user.exhibits
        current_date = datetime.now()
        if artwork:
            """check artwork exists"""
            exhibit_art = Exhibit_Artwork.query.filter_by(artwork_id=artwork.id).first()
            if exhibit and (exhibit.start_date <= current_date and exhibit.end_date >= current_date)  and exhibit_art:
                flash("Can't add to general exhibit when exhibit is ongoing", category="danger")
                return redirect(url_for('user_dashboard', username=current_user.username))
            artwork.type = "general_artwork"
            db.session.commit()
            flash("Successfully added artwork to general artworks", category="success")
            return redirect(url_for('user_dashboard', username=current_user.username))
        else:
            flash("Artwork not found", category="danger")
            return redirect(url_for('user_dashboard', username=current_user.username))
