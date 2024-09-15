from .models import Category, User


def load_categories():
    return Category.query.all()


def fetch_user(id):
    return User.query.filter(User.is_active.__eq__(True), User.id.__eq__(id)).first()


def create_user(username, email, password, **kwargs):
    user = User(
        username=username,
        email=email,
        password=password,
        **kwargs
    )
    user.save()
    return user


def auth_user(email, password):
    user = User.query.filter(User.email.__eq__(email)).first()
    return user if user and user.check_password(password=password) else None