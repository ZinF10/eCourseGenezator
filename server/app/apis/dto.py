from flask_restx import Namespace, fields


class CategoryDto:
    api = Namespace('categories', description='Category related operations')
    category = api.model('Category', {
        'name': fields.String(required=True, description='category name'),
    })