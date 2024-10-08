from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_login import LoginManager

from apis import api
from .config import config_by_name
from .admin import admin_manager
from .models import db
from .dao import fetch_user
from .controllers import auth_admin

flask_bcrypt = Bcrypt()
login_manager = LoginManager()


def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    CORS(app=app, resources={r"/*": {"origins": "*"}})
    
    db.init_app(app=app)
    api.init_app(app=app)
    admin_manager.init_app(app=app)
    flask_bcrypt.init_app(app=app)
    login_manager.init_app(app=app)
    
    @login_manager.user_loader
    def load_user(user_id):
        return fetch_user(id=user_id)

    app.add_url_rule('/auth-admin', view_func=auth_admin, methods=['POST'])
    
    return app