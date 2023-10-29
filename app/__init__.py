from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from datetime import datetime


app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
cors = CORS(app)
login_manager.login_view = "user_login"
login_manager.login_message = "info"


from app.routes import home_route, artworks_route, create_user_route, exhibits_route
from app.routes import upload_artwork_route, user_dashboard_route, user_delete_route
from app.routes import user_login_route, user_logout_route, user_profile_route
from app.routes import delete_artwork_route, edit_artwork_route, shopping_cart_route
from app import apis
