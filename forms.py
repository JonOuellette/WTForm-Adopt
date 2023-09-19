from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, NumberRange, URL, Optional

class AddPetForm(FlaskForm):
    """Form to add pets"""

    pet_name = StringField("Pet Name", validators = [InputRequired])

    species = SelectField("Pet Name", choices=[("cat" = "Cat"), ("dog" = "Dog"), ("porcupine"= "Porcubine")])

    pet_image = StringField("Photo URL", validators=[Optional(), URL()])

    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])

    notes = TextAreaField("Comments", validators=[Optional()])

class EditPetForm(FlaskForm):
    """Form to edit existing pet information"""

    pet_image = StringField("Photo URL", validators=[Optional(), URL()])

    notes = TextAreaField("Comments", validators=[Optional()])

    available = BooleanField("Available?")