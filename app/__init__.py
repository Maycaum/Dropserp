from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object('config')


db = SQLAlchemy(app)
migrate = Migrate(app, db) # A instancia do migrate cuida das migrações pra isso ele recebe a aplicação e o banco


from app.models import tables
from app.controllers import default