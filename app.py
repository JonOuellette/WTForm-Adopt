from flask import Flask, redirect, render_template, flash, url_for
from flask_debugtoolbar import DebugToolbarExtension
from forms import AddPetForm
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


@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Adds a pet."""

    form = AddPetForm()

    if form.validate_on_submit():
        pet_name = form.pet_name.data
        species = form.species.data
        pet_image = form.pet_image.data
        age = form.age.data
        notes = form.notes.data
        pet = Pet(pet_name= pet_name, species=species, pet_image=pet_image, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        return redirect(url_for('pets_list'))
    
    else: 
        return render_template("add_pet_form.html", form = form)
    
@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edits the pet information"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm()