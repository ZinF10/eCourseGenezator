from .models import Category


def load_categories():
    return Category.query.all()