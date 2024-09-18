from flask_restx import Resource

from core import dao
from .dto import CourseDTO

api = CourseDTO.api
model = CourseDTO.model
details = CourseDTO.details
parser = CourseDTO.parser
pagination = CourseDTO.pagination

@api.route('/')
class CourseList(Resource):
    @api.doc(params={
        'category': 'An Category ID',
        'keyword': 'Keyword to search for',
        'from_price': 'Minimum price',
        'to_price': 'Maximum price',
        'page': 'Page number for pagination'
    }, security="jwt")
    @api.expect(parser)
    @api.marshal_with(pagination, code=200)
    @api.doc('list_courses')
    def get(self):
        """ Get all courses """
        args = parser.parse_args()
        data = dao.load_courses(**args)
        response = {
            'count': data['count'],
            'next': data['next_page'],
            'previous': data['prev_page'],
            'results': data['results'],
        }
        print(response)
        return response
    
    
@api.route('/<int:id>')
@api.response(404, 'Not found')
@api.param('id', 'The course identifier')
class Course(Resource):
    @api.marshal_with(details, code=200)
    @api.doc('get_course')
    def get(self, id):
        """ Get course details """
        return dao.load_course(course_id=id) or api.abort(404, "Course {} doesn't exist".format(id))