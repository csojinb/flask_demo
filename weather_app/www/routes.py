from flask import Blueprint, render_template, request, url_for, redirect

from forms import LocationForm

blueprint = Blueprint('weather', __name__, template_folder='templates')


@blueprint.route('/', methods=['GET', 'POST'])
def get_location():

    location_form = LocationForm(csrf_enabled=False)
    if request.method == 'POST' and location_form.validate():
        location = location_form.zip_code.data
        print location
        return redirect(url_for('.show_location', location=location))

    return render_template('index.html', form=location_form)

@blueprint.route('/<location>')
def show_location(location):

    return render_template('location_weather.html', location=location)