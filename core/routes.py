from flask import render_template
from core import app


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Ton"}
    return render_template("index.html", title="Home", user=user)
