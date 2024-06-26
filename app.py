from flask import Flask, render_template, redirect,request, session
from flask_session import Session
from departureClasses import getDepartures,departure
from markupsafe import escape 
from datetime import datetime

#Command to run the app is: python -m flask --app app --debug run
#Activating virtual environment departureDash\scripts\activate
app = Flask(__name__)
app.config["SECRET_KEY"] = "any random string"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
retrieveDepartures = getDepartures()
#app.jinja_env.globals.update(search=search)

@app.route("/")
def index():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    #If the API call for the randomly selected station fails we'll simply try it again by redirecting to the index route again
    try:
        randomStation,randomDepartures = retrieveDepartures.getRandomDepartures()
    except:
        return redirect('/')
    session['randomStation'] = randomStation
    return render_template("index.html",a_variable = "No station selected",departures = randomDepartures,length = len,order = orderConvert, enumerate = enumerate, str = str, time = current_time)

@app.route("/<requestedStation>")
def displayDepartures(requestedStation):
    requestedStation = escape(requestedStation)
    requestedStationsDepartures = retrieveDepartures.query(requestedStation.upper())
    session['currentStationCode'] = retrieveDepartures.convertStationToCode(requestedStation)
    session['currentStation'] = retrieveDepartures.convertCodeToStation(requestedStation)
    return render_template("board.html",departures = requestedStationsDepartures, stationCode = retrieveDepartures.getStation(),length = len,stationTitle = requestedStation.upper(),order = orderConvert, enumerate = enumerate, str = str)

@app.route('/board',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        json_result = dict(result)
        print(json_result)
        requestedStation = escape(json_result.get("stationBox"))
        return redirect(f'/{requestedStation}')
@app.route('/handleOptions',methods=['POST'])
def handle_options():
    if request.method == 'POST':
        result = request.form
        json_result = dict(result)
        if json_result.get("button") == "home":
            return redirect("/")
        else:
            return redirect(f'/{json_result.get("button")}')
@app.errorhandler(404)
def page_not_found(error):
    return redirect('/XXX')
@app.route('/width', methods=['POST'])
def width():
    if request.method == 'POST':
        result = request.form
        json_result = dict(result)
        print(json_result)
        session['width'] = float(str(json_result.get('width'))) // 10
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
        