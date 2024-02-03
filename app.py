from flask import Flask, render_template
from departureTemplate import departure #Custom departure object

#Command to run the app is: python -m flask --app app run
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")