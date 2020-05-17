from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager    
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager

app =  Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

migrate = Migrate(app, db) #Manages migrations

manager = Manager(app) #Manages commands
manager.add_command('db', MigrateCommand)

login_manager = LoginManager()
login_manager.init_app(app)

from app.models import dbconfig, forms
from app.controllers import default
from app.controllers import useraccount