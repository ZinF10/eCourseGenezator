from flask_restx import Namespace, fields

class BaseDTO:
    """Base Data Transfer Object for common fields."""
    api = Namespace('base')
    model = api.model('Base', {
        'id': fields.Integer(readonly=True, description='Unique ID'),
        'is_active': fields.Boolean(description='Active'),
        'date_created': fields.DateTime(dt_format='iso8601'),
    })
    

class CategoryDTO(BaseDTO):
    """Category Data Transfer Object."""
    api = Namespace('categories', description='Category related operations')
    model = api.inherit('Category', BaseDTO.model, {
        'name': fields.String,
    })