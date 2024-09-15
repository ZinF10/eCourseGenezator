from flask_restx import Resource

from core import dao
from .dto import CategoryDTO

api = CategoryDTO.api
model = CategoryDTO.model

@api.route('/')
class CategoryList(Resource):
    @api.marshal_with(model, code=200)
    def get(self):
        """ Get all categories """
        return dao.load_categories()