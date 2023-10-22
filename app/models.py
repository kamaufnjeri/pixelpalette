from app import db, login_manager, bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(64), nullable=False, index=True, unique=True)
    first_name = db.Column(db.String(15),nullable=False, index=True)
    last_name = db.Column(db.String(15),nullable=False, index=True)
    email_address = db.Column(db.String(120), nullable=False, index=True, unique=True)
    category = db.Column(db.String(30), nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    
    def check_password_correct(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)
    
    def __repr__(self):
        # Change printing of objects of class User to help in debugging
        return f'User {self.username}'