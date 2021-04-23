from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from config import Config
from pymongo import MongoClient

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

# Create client for Mongodb
client = MongoClient()
# connect to local host
client = MongoClient(Config.URI)

# Create Login manager
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'warning'

from project.models import *
db.create_all()

import project.views
