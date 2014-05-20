from flask import Blueprint, render_template, request, url_for, redirect

blueprint = Blueprint('weather', __name__, template_folder='templates')


@blueprint.route('/', methods=['GET', 'POST'])
def get_location():
    if request.method == 'POST':
        location = request.form['zip_code']
        return redirect(url_for('.show_location', location=location))

    return render_template('index.html')

@blueprint.route('/<location>')
def show_location(location):

    return render_template('location_weather.html', location=location)