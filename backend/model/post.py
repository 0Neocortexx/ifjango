from config import *
from model.user import *

class Post(db.model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String, nullable = False)
    user_email = db.Column(db.String(254), db.ForeignKey(User.email))
    user = db.relationship('User')

    def __str__(self):
        return f'ID: {self.id}, content: {self.content}, email do usuário: {self.user_email}'
    
    def json(self):
        return {
            'id': self.id,
            'content': self.content,

            'user_email': self.user_email,
            'user_name': self.user.name
        }