from flask import (
    Flask,
    request,
    render_template
)


app = FLASK(__name__)


@app.get("/")
def index():
    return "<h1>Test!<h/1>"

@app.get("/users/add")