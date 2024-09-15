from flask import Flask

from apis import api
from .config import config_by_name
from .admin import admin_manager
from .models import db


def create_app(config_name: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    
    db.init_app(app=app)
    api.init_app(app=app)
    admin_manager.init_app(app=app)
    
    return app