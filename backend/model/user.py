from config import *
from model.post import *

class User(db.model):
    email = db.Column(db.String(254), primary_key = True, nullable = False)
    name = db.Column(db.String(254), nullable = False)
    password = db.Column(db.String(254), nullable = False)

    content_id = db.Column(db.Integer, db.ForeignKey(Post.id), nullable = True)
    post = db.relationship('Post')


    def __str__(self):
        return f'Email: {self.email}, Name: {self.name}, Password: {self.password}'

    def json(self):
        return {
            'email': self.email,
            'name': self.name,
            'password': self.password,
            'content_id': self.content_id
        }

