import os
from flask import Flask, render_template, redirect
from time import sleep

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/teste")
def index():
    return redirect("http://www.example.com", code=302)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port)