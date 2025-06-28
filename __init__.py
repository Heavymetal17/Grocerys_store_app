from flask import Flask
from flask import render_template
from flask import request

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # Replace with a strong secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Update the database URI if needed

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
