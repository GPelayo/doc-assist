from application import db


class Changes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(35), unique=True)
    paragraph_location = db.Column(db.Integer)
    char_location = db.Column(db.Integer)

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
