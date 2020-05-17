# -*- coding: utf-8 -*
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import db
from app import login_manager


class User(db.Model):
    __titlename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def user_loader(self, callback):
        return callback

    def is_active(self):
        return True
    
    def get_id(user_id):
        return str(user_id)

    @login_manager.user_loader
    def load_user(user_id):
        return User.get_id(user_id)

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def __init__(self , username, email, password):
        self.username = username
        self.email = email
        self.password = password
    
    def __repr__(self):
        return '<User %r>' % self.username
        

class Post(db.Model):
    __titlename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))

    user = db.relationship('User', foreign_keys=user_id)

    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id
    
    def __repr__(self):
        return '<Post %r>' % self.id
    

class Follow(db.Model):
    __tablename__ = "follow" 

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    follower_id = db.Column(db.Integer, db.ForeignKey(User.id))

    user = db.relationship('User', foreign_keys=user_id)
    follower = db.relationship('User', foreign_keys=follower_id)


    