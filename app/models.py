from app import db, login_manager, bcrypt
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(64), nullable=False, index=True, unique=True)
    first_name = db.Column(db.String(15), nullable=False, index=True)
    last_name = db.Column(db.String(15), nullable=False, index=True)
    email_address = db.Column(db.String(120), nullable=False, index=True, unique=True)
    category = db.Column(db.String(30), nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    cart = db.relationship('ShoppingCart', backref='user', uselist=False, lazy=True)
    purchase_items = db.relationship('PurchaseItem', backref="purchaser", lazy=True)
    owner_artworks = db.relationship('Artwork', backref="owner", lazy=True)

    def check_password_correct(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

    def __repr__(self):
        return f'User {self.username}'

class Artwork(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), unique=True, index=True, nullable=False)
    description = db.Column(db.String(1024), index=True, nullable=False)
    price = db.Column(db.Integer(), index=True, nullable=False)
    category = db.Column(db.String(), index=True, nullable=False)
    artwork_url = db.Column(db.String(), unique=True, index=True, nullable=False)
    owner_id = db.Column(db.Integer(), db.ForeignKey('user.id'))

class ShoppingCart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    total_amount = db.Column(db.Integer, nullable=False, default=0)
    purchase_date = db.Column(db.TIMESTAMP, server_default=db.func.now())
    purchase_items = db.relationship('PurchaseItem', backref="shopping_cart", lazy=True)

class PurchaseItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, default=1)

    # Explicit foreign key constraints
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    cart_id = db.Column(db.Integer, db.ForeignKey('shopping_cart.id'))
    artwork_id = db.Column(db.Integer, db.ForeignKey('artwork.id'))

    artwork = db.relationship('Artwork', backref="artwork", lazy=True)

    def __repr__(self):
        return f'PurchaseItem {self.id}'
