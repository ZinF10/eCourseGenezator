from .models import Category, User, Course


def load_categories():
    return Category.query.filter(Category.is_active.__eq__(True)).order_by(Category.id.desc()).all()


def load_courses():
    return Course.query.filter(Course.is_active.__eq__(True)).order_by(Course.id.desc()).all()


def load_course(course_id):
    return Course.query.get_or_404(int(course_id))


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