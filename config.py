import os.path
basedir = os.path.abspath(os.path.dirname(__file__))
from flask.ext.script import Manager, Server
from app import app

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir, 'storage.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY ='uma-chave-bem-segura'

UPLOAD_FOLDER = os.path.join(basedir, '/app/static/product_image/')
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
