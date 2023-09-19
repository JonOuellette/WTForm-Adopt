from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from forms import
from models import db, connect_db, Pet

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "petadopt123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)
app.app_context().push()

connect_db(app)
db.create_all()

@app.route('/')
def pets_list():
    """Displays list of pets"""
    
    pets = Pet.query.all()
    return render_template('pet_listing.html', pets= pets)


