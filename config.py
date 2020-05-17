from app import app
from flask import Flask
import os.path
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'storage.db') 

SECRET_KEY = "19970210"