from flask_restx import Resource

from core import dao
from .dto import CourseDTO

api = CourseDTO.api
model = CourseDTO.model

@api.route('/')
class CourseList(Resource):
    @api.marshal_with(model, code=200, envelope="results", as_list=True)
    @api.doc('list_courses')
    def get(self):
        """ Get all courses """
        return dao.load_courses()
    
    
@api.route('/<int:id>')
@api.response(404, 'Not found')
@api.param('id', 'The course identifier')
class Course(Resource):
    @api.marshal_with(model, code=200)
    @api.doc('get_course')
    def get(self, id):
        """ Get course details """
        return dao.load_course(course_id=id) or api.abort(404, "Course {} doesn't exist".format(id))