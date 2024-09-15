from flask.cli import FlaskGroup
from flask_migrate import Migrate

from core import create_app, db

app = create_app('dev')

manager = FlaskGroup(create_app=lambda: create_app('dev'))

migrate = Migrate(app=app, db=db)

from core.models import Category

if __name__ == '__main__':
    manager()