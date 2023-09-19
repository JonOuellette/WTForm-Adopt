""" Model for the adopt app"""

from flask_sqlalchemy import SQLAlchemy

DEFAULT_IMAGE = "https://cdn.pixabay.com/photo/2016/04/07/18/57/silhouette-1314467_640.png"

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

    def image_url(self):
        """Used in url_for method to return image - default image or user provided"""
        return self.pet_image or DEFAULT_IMAGE

def connect_db(app):
    """Connects database to Flask app"""
    db.app = app
    db.init_app(app)