from flask_restx import Namespace, fields, reqparse

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
    

class CourseDTO(BaseDTO):
    """Course Data Transfer Object."""
    api = Namespace('courses', description='Course related operations')
    model = api.inherit('Course', BaseDTO.model, {
        'subject': fields.String(required=True, description='Course subject'),
        'price': fields.Float,
        'category': fields.String(required=True, description='Course category'),
    })
    details = api.inherit('Course Details', model, {
        'description': fields.String(required=True, description='Course description')
    })
    parser = reqparse.RequestParser(bundle_errors=True)
    parser.add_argument('category', type=int, required=False, help='Category ID')
    parser.add_argument('keyword', type=str, required=False, help='Search keyword')
    parser.add_argument('from_price', type=float, required=False, help='Minimum price')
    parser.add_argument('to_price', type=float, required=False, help='Maximum price')