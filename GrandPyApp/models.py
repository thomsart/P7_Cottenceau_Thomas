from flask_sqlalchemy import SQLAlchemy

from .views import app

# create the database connection object
db = SQLAlchemy(app)

class Content(db.Model):

    id =  db.Column(db.Integer, primary_key=True)
    speech = db.Column(db.String(100), nullable=False)

    def __init__(self, grandpy_sentence):
        self.speech = grandpy_sentence

db.create_all()