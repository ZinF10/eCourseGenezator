from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_bcrypt import generate_password_hash, check_password_hash
from datetime import datetime, timezone

db = SQLAlchemy()

class BaseModel(db.Model):
    __abstract__ = True
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    is_active = db.Column(db.Boolean, default=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    
class Category(BaseModel):
    name = db.Column(db.String(50), unique=True)

    def __str__(self):
        return self.name
    

class User(BaseModel, UserMixin):
    email = db.Column(db.String(255), unique=True)
    is_admin = db.Column(db.Boolean, default=False)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(255))
    first_name = db.Column(db.String(80), nullable=True)
    last_name = db.Column(db.String(80), nullable=True)
    last_seen = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def __init__(self, password, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.password = generate_password_hash(password).decode('utf-8')

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password, password)

    def __str__(self):
        return self.username