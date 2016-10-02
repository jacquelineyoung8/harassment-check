from flask import Flask
from flask import render_template

app = Flask(__name__)

import json

from datetime import date
from datetime import timedelta

@app.route("/")
def index():


    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
	

    return render_template("index.html")


if __name__ == "__main__":
    app.run('0.0.0.0')


