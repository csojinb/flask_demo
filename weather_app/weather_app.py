import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/weather', methods=['GET', 'POST'])
def get_location():
    if request.method == 'POST':
        location = request.form['zip_code']
        return redirect(url_for('show_location', location=location))

    return render_template('index.html')

@app.route('/weather/<location>')
def show_location(location):

    return render_template('location_weather.html', location=location)

if __name__ == '__main__':
    app.debug = True
    app.run()