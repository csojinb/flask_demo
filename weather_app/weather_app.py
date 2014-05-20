import os
from flask import Flask, render_template, request, redirect, url_for

from www.routes import blueprint

app = Flask(__name__)
app.register_blueprint(blueprint, url_prefix='/weather')


if __name__ == '__main__':
    app.debug = True
    app.run()