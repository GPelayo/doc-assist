from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('default.cfg')
db = SQLAlchemy(app)

import models
import routes