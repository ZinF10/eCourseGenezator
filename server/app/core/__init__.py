from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from apis import api
from .config import config_by_name
from .admin import admin_manager
from .models import db

flask_bcrypt = Bcrypt()
login_manager = LoginManager()


def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    
    db.init_app(app=app)
    api.init_app(app=app)
    admin_manager.init_app(app=app)
    flask_bcrypt.init_app(app=app)
    login_manager.init_app(app=app)
    
    return app