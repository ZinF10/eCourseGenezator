from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import SecureForm

from .models import db, Category, Course
from .config import Config

class BaseModelView(ModelView):
    form_base_class = SecureForm
    column_labels = {
        "is_active": "Active",
    }
    column_list = ["is_active", "date_created", "date_updated"]
    column_filters = ["is_active"]
    column_editable_list = ["is_active"]
    column_sortable_list = ["date_created"]
    create_modal = True
    edit_modal = True
    can_view_details = True
    can_export = True
    can_delete = True
    page_size = Config.PAGE_SIZE


class CategoryAdmin(BaseModelView):
    column_list = ["name", "courses"] + BaseModelView.column_list
    column_sortable_list = ["name"] + BaseModelView.column_sortable_list
    column_editable_list = ["name"] + BaseModelView.column_editable_list


class CourseAdmin(BaseModelView):
    column_list = ["subject", "category"] + BaseModelView.column_list
    column_sortable_list = ["subject"] + BaseModelView.column_sortable_list
    column_editable_list = ["subject"] + BaseModelView.column_editable_list


admin_manager = Admin(name="eCourse 🎓", template_mode='bootstrap4')
admin_manager.add_view(CategoryAdmin(Category, db.session, category="Management"))
admin_manager.add_view(CourseAdmin(Course, db.session, category="Management"))