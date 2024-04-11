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
    session["currentStation"] = retrieveDepartures.convertStation(requestedStation)
    return render_template("board.html",departures = requestedStationsDepartures, stationCode = retrieveDepartures.getStation(),length = len, lengthArg = session['lengthArg'],stationTitle = requestedStation.upper(),order = orderConvert, enumerate = enumerate, str = str)

@app.route('/board',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        json_result = dict(result)
        print(json_result)
        requestedStation = escape(json_result.get("stationBox"))
        session["currentStation"] = requestedStation
        displayDepartures(requestedStation)
        return redirect(f'/{requestedStation}')
@app.route('/handleOptions',methods=['POST'])
def handle_options():
    if request.method == 'POST':
        result = request.form
        json_result = dict(result)
        print(json_result)
        session["currentStation"] = retrieveDepartures.getStation()
        if result.get("button") == "home":
            return redirect("/")
        else:
            return redirect(f'/{session["currentStation"]}')
@app.errorhandler(404)
def page_not_found(error):
    return redirect('/XXX')
@app.route('/width', methods=['POST'])
def width():
    if request.method == 'POST':
        result = request.form
        json_result = dict(result)
        print(json_result)
        session['lengthArg'] = int((json_result.get('width'))) #this needs to be altered
        return ('', 204)
def orderConvert(n):  
        num = str(n)
        if num == "11" or num == "12" or num == "13":
            return num+"th"
        if num[-1] == "1":
            return num+"st"
        if num[-1] == "2":
            return num+"nd"
        if num[-1] == "3":
            return num+"rd"
        else:
            return num+"th" 
        