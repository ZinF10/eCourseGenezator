from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from .models import db, Category


admin_manager = Admin(name="eCourse 🎓", template_mode='bootstrap4')
admin_manager.add_view(ModelView(Category, db.session, category="Management"))