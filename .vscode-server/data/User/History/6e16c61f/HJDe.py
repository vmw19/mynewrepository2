from flask import Flask


app = FLASK(__name__)


@app.get("/")
def index():
    return "<h1>Test!<h/1>"