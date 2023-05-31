from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
import uuid

from werkzeug.security import generate_password_hash
import secrets

from datetime import datetime

from flask_login import UserMixin, LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow()

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(user_id)

# class User(db.Model, UserMixin):
#     id = db.Column(db.String, primary_key = True)
#     first_name = db.Column(db.String(150), nullable = True, default = '')
#     last_name = db.Column(db.String(150), nullable = True, default = '')
#     email = db.Column(db.String(150), nullable = False)
#     password = db.Column(db.String, nullable = True)
#     g_auth_verify = db.Column(db.Boolean, default = False)
#     token = db.Column(db.String, default = '', unique = True)
#     date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
#     task = db.relationship('Task', backref = 'owner', lazy = True)

#     def __init__(self, email, first_name = '', last_name = '', id = '', password = '', token = '', g_auth_verify = False):
#         self.id = self.set_id()
#         self.first_name = first_name
#         self.last_name = last_name
#         self.password = self.set_password(password)
#         self.email = email
#         self.token = self.set_token(24)
#         self.g_auth_verify = g_auth_verify

#     def set_token(self, length):
#         return secrets.token_hex(length)

#     def set_id(self):
#         return str(uuid.uuid4())

#     def set_password(self, password):
#         self.pw_hash = generate_password_hash(password)
#         return self.pw_hash
    
#     def __repr__(self):
#         return f"User {self.email} has been added to the database!"
    
class Task(db.Model):
    id = db.Column(db.String, primary_key = True)
    task_name = db.Column(db.String(150), nullable = True)
    task_content = db.Column(db.String, nullable = True)
    days_of_week = db.Column(db.String, nullable = False)
    repeat_weekly = db.Column(db.Boolean, nullable = False, default = False)
    user_token = db.Column(db.String, nullable = False)

    def __init__(self, task_name, task_content, days_of_week, user_token, repeat_weekly=False):
        self.id = self.set_id()
        self.task_name = task_name
        self.task_content = task_content
        self.days_of_week = days_of_week
        self.user_token = user_token
        self.repeat_weekly = repeat_weekly

    def set_id(self):
        return secrets.token_urlsafe()
    
    def __repr__(self):
        return "Task added to your calendar!"
    
class TaskSchema(ma.Schema):
    class Meta:
        fields = ['id', 'task_name', 'task_content', 'days_of_week', 'repeat_weekly', 'user_token']

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)