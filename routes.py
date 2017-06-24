from application import app
from models import Changes

@app.route('/')
def index():
    return "\t".join(map(str, Changes.query.all()))