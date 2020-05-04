from app import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey

class User(db.Model):
    __titlename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __intit__(self, id, username, email, password):
        self.id =  id
        self.username = username
        self.email = email
        self.password = password
    
    def __repr__(self):
        return '<Post %r>' % self.username
        
    