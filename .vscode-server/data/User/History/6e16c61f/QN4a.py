from flask import (
    Flask,
    request,
    render_template
)


app = FLASK(__name__)
BACKEND_URL = "http://127/0.0.1:5000"

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/users/new")
def create_user():
    return render_template("new_user.html")

@app.get("/users")
def user_list():
    url = "%/%"
    response - requests.get()
    return render_template("user_list.html")