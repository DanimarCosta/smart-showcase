import os
from flask import Flask, render_template, redirect

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("index.html")

#Sub Pages
@app.route("/ensino")
def ensino():
    return render_template("ensino.html")

@app.route("/cursos")
def cursos():
    return render_template("cursos.html")

@app.route("/tour")
def tour():
    return render_template("tour.html")

@app.route("/maps")
def maps():
    return render_template("maps.html")

def nunsei():
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port)
