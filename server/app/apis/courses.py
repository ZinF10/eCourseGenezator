from flask_restx import Resource

from core import dao
from .dto import CourseDTO

api = CourseDTO.api
model = CourseDTO.model
details = CourseDTO.details
parser = CourseDTO.parser

@api.route('/')
class CourseList(Resource):
    @api.doc(params={
        'category': 'An Category ID',
        'keyword': 'Keyword to search for',
        'from_price': 'Minimum price',
        'to_price': 'Maximum price',
    }, security="jwt")
    @api.expect(parser)
    @api.marshal_with(model, code=200, envelope="results", as_list=True)
    @api.doc('list_courses')
    def get(self):
        """ Get all courses """
        args = parser.parse_args()
        return dao.load_courses(**args)
    
    
@api.route('/<int:id>')
@api.response(404, 'Not found')
@api.param('id', 'The course identifier')
class Course(Resource):
    @api.marshal_with(details, code=200)
    @api.doc('get_course')
    def get(self, id):
        """ Get course details """
        return dao.load_course(course_id=id) or api.abort(404, "Course {} doesn't exist".format(id))