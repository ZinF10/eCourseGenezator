import getpass
from flask.cli import FlaskGroup
from flask_migrate import Migrate

from core import create_app, db, dao
from core.controllers import load_user

app = create_app('dev')

manager = FlaskGroup(create_app=lambda: create_app('dev'))

migrate = Migrate(app=app, db=db)

from core.models import Category, User


@manager.command("create_admin")
def create_admin():
    """Creates the admin user."""
    username = input("Username: ")
    email = input("Email address: ")
    password = getpass.getpass("Password: ")
    confirm_password = getpass.getpass("Password (again): ")
    
    if password != confirm_password:
        print("Passwords don't match")
    else:
        try:
            dao.create_user(username=username, email=email, password=password, is_admin=True)
            print(f"Admin with email {email} created successfully!")
        except Exception:
            print("Couldn't create admin user.")


if __name__ == '__main__':
    manager()