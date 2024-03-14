from flask import Flask, render_template, redirect,request
from departureTemplate import departure #Custom departure object
from departureFactory import getDepartures

#Command to run the app is: python -m flask --app app run
#Activating virtual environment departureDash\scripts\activate
app = Flask(__name__)
retrieveDepartures = getDepartures()
#app.jinja_env.globals.update(search=search)

@app.route("/")
def index():
    return render_template("index.html",a_variable = "No station selected")

@app.route("/<requestedStation>")
def displayDepartures(requestedStation):
    requestedStationsDepartures = retrieveDepartures.query(requestedStation.upper())
    return render_template("board.html",departures = requestedStationsDepartures)

@app.route('/board',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        json_result = dict(result)
        print(json_result)
        requestedStation = json_result.get("stationBox")
        return redirect(f'/{requestedStation}')