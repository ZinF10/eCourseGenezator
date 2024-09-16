from flask_restx import Api

from .dto import BaseDTO
from .categories import api as category_ns
from .courses import api as course_ns


api = Api(
    contact="zin.it.dev@gmail.com",
    contact_email="zin.it.dev@gmail.com",
    version='1.0',
    title='eCourse 🎓',
    description='APIs for eCourse 🎓',
    license='Apache 2.0',
    ordered=True
)

api.add_namespace(BaseDTO.api)
api.add_namespace(category_ns)
api.add_namespace(course_ns)