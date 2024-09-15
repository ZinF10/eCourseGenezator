from flask_restx import Api

from .categories import api as category_ns


api = Api(
    contact="zin.it.dev@gmail.com",
    contact_email="zin.it.dev@gmail.com",
    version='1.0',
    title='eCourse 🎓',
    description='APIs for eCourse 🎓',
    license='Apache 2.0',
    ordered=True
)

api.add_namespace(category_ns)