import os
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/weather', methods=['GET', 'POST'])
def get_location():
    if request.method == 'POST':
        location = request.form['zip_code']

    return render_template('index.html', location=location)


if __name__ == '__main__':
    app.debug = True
    app.run()