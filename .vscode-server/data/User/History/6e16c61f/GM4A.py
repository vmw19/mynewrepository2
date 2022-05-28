from flask import (
    Flask,
    request,
    render_template
)


app = FLASK(__name__)


@app.get("/")
def index():
    return render_template("index

@app.get("/users/new")
def create_user():
    return render_template("new_user.html")

@app.get("/users")
def user_list():
    return render_template("user_list.html")