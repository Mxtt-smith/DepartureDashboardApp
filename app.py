from flask import Flask, render_template
from departureTemplate import departure #Custom departure object
from departureFactory import getDepartures

#Command to run the app is: python -m flask --app app run
app = Flask(__name__)
retrieveDepartures = getDepartures()

@app.route("/")
def index():
    a = "helloooooo"
    return render_template("index.html",a_variable = a)

@app.route("/<requestedStation>")
def displayDepartures(requestedStation):
    d = retrieveDepartures.query(requestedStation)
    return render_template("index.html",a_variable = d[0].getDestination())
    
