import os
from flask import Flask

app = Flask(__name__)


@app.route('/weather')
def hello_world():
    return "Hey look our site is running on local! WHOO!"

if __name__ == '__main__':
    app.run()