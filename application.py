from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('default.cfg')


try:
    import local_settings
    HOST_ADDRESS = local_settings.HOST_ADDRESS
except ImportError:
    HOST_ADDRESS = "localhost"

db = SQLAlchemy(app)

import models
import routes