import unittest
from flask_testing import TestCase

from core import create_app, db


class BaseTestCase(TestCase):
    def create_app(self):
        return create_app('test')

    def setUp(self):
        self.app = self.create_app()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


if __name__ == '__main__':
    unittest.main()