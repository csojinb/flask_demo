from flask import Blueprint, render_template, request, url_for, redirect
from get_weather import get_weather

from forms import LocationForm

blueprint = Blueprint('weather', __name__, template_folder='templates')


@blueprint.route('/', methods=['GET', 'POST'])
def get_location():

    location_form = LocationForm(csrf_enabled=False)

    if request.method == 'POST' and location_form.validate():
        location = location_form.zip_code.data

        return redirect(url_for('.show_weather', location=location))

    return render_template('index.html', form=location_form)


@blueprint.route('/<location>')
def show_weather(location):
    weather_info = get_weather(location)
    back_link = url_for('.get_location')

    if 'error' in weather_info.keys():
        return render_template('error.html',
                               location=location,
                               back_link=back_link)
    else:
        return render_template('location_weather.html',
            weather=weather_info,
            back_link=back_link)