from application import app
from models import Changes
from flask import render_template
from os import path
from textutils.preview import get_sample
base = path.dirname(__file__)


@app.route('/')
def index():
    return render_template(path.join("preview.html"),
                           paragraphs=get_sample())
