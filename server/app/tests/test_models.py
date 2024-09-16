import unittest

from core.models import Category
from tests.base import BaseTestCase


class TestCategoryModel(BaseTestCase):
    def test_create_model(self):
        category = Category(name='Networking')
        category.save()
        self.assertIsNotNone(Category.query.filter_by(name='Networking').first())


if __name__ == '__main__':
    unittest.main()