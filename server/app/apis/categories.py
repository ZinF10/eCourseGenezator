from flask_restx import Resource

from core import dao
from .dto import CategoryDto

api = CategoryDto.api
model = CategoryDto.category


@api.route('/')
class CategoryList(Resource):
    @api.marshal_with(model, code=200, as_list=True)
    def get(self):
        """ Get all categories """
        return dao.load_categories()