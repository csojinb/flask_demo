## Flask Demo & Tutorial
==========
Prepared for the 2014 Code for Progress fellowship program, by [Clara Bennett](https://github.com/csojinb) and [Emily Williamson](https://github.com/districtem)

### Overview
This tutorial goes through building a simple weather application using Python and Flask. You can follow it by starting at the beginning of the git history and checking out successive commits that begin with "CHECKPOINT".

### Installing the Requirements

The app has three main dependencies: Flask, WTForms, and requests. It also depends on flask_wtf, which is a Flask plugin for WTForms.

To install the dependencies, simply run
```
pip install requirements.txt
```

### Run the App
To run the application, at any point in the git history after the "hello world" Flask app is created, run
```
python weather_app/weather_app.py
```

Then, open your browser to visit [http://localhost:5000/weather](http://localhost:5000/weather)
