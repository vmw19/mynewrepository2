from flask import (
    Flask,
    request,
    render_template
)


app = FLASK(__name__)


@app.get("/")
def index():
    return "<h1>Test!<h/1>"

@app.get("/users/new")
def create_user():
    return render_template("new_user.html")

@app.get("/")