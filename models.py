""" Model for the adopt app"""
from flask_sqlalchemy import SQLAlchemy

DEFAULT_IMAGE = "https://pixabay.com/illustrations/silhouette-imprint-paw-foot-track-1314467/"

db = SQLAlchemy()

class Pet(db.Model):

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key = True, autoincrement= True)
    pet_name = db.Column(db.Text, nullable = False )
    species = db.Column(db.Text, nullable = False)
    pet_image = db.Column(db.Text, nullable = True)
    age = db.Column(db.Integer, nullable = True)
    notes = db.Column(db.Text, nullable = True)
    available = db.Column(db.Boolean, nullable = False, default = True)

def connect_db(app):
    """Connects database to Flask app"""
    db.app = app
    db.init_app(app)