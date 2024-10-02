from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def start():
   return "My first flask app"

@app.route("/home")
def home():
   return render_template("index.html")

