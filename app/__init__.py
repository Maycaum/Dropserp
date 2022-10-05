from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_ngrok2 import run_with_ngrok

app = Flask(__name__)
app.config.from_object('config')
#run_with_ngrok(app, auth_token='2FgufYFYVmF47Oh5O0EJ5mraGg9_4KUBtPyfTWMNTmQ3WmUiB')

db = SQLAlchemy(app)
migrate = Migrate(app, db) # A instancia do migrate cuida das migrações pra isso ele recebe a aplicação e o banco


lm = LoginManager()
lm.init_app(app)

from app.models import tables, form
from app.controllers import default