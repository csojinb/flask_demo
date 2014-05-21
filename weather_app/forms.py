from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import Regexp, DataRequired

class LocationForm(Form):
    zip_code = TextField('zip_code',
        validators=[DataRequired(),
        Regexp(r'^\d{5}(?:[-\s]\d{4})?$', message='Please enter valid zip code.')],
        description = {'placeholder': 'Zip Code'})