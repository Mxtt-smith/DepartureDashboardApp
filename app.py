from flask import Flask, render_template, redirect,request, session
from departureTemplate import departure #Custom departure object
from departureFactory import getDepartures
from markupsafe import escape 

#Command to run the app is: python -m flask --app app --debug run
#Activating virtual environment departureDash\scripts\activate
app = Flask(__name__)
app.config["SECRET_KEY"] = "any random string"
retrieveDepartures = getDepartures()
#app.jinja_env.globals.update(search=search)

@app.route("/")
def index():
    return render_template("index.html",a_variable = "No station selected")

@app.route("/<requestedStation>")
def displayDepartures(requestedStation):
    requestedStationsDepartures = retrieveDepartures.query(requestedStation.upper())
    return render_template("board.html",departures = requestedStationsDepartures, stationTitle = retrieveDepartures.getStation())

@app.route('/board',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        json_result = dict(result)
        print(json_result)
        requestedStation = escape(json_result.get("stationBox"))
        session["currentStation"] = requestedStation
        return redirect(f'/{requestedStation}')
@app.route('/handleOptions',methods=['POST'])
def handle_options():
    if request.method == 'POST':
        result = request.form
        json_result = dict(result)
        if result.get("opButton") == "back":
            return redirect("/")
        else:
            return redirect(f'/{session["currentStation"]}')
@app.errorhandler(404)
def page_not_found(error):
    return redirect('/XXX')
