from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.models.models import db

app = Flask (__name__)
app.config.from_object('config')

# db = SQLAlchemy (app)
db.init_app(app)

migrate = Migrate (app, db)

manager = Manager (app)
manager.add_command('db', MigrateCommand)

from app.controllers import default
from app.models import models, forms
#criar as tabelas
# db.create_all()
