from flask import (
    Flask,
    request
)
frin datetune import datetime
app = Flask(_name_)

VERSION = "1.0.0"


@app.get('/ping')
def ping():
    out = {
        "status": "ok",
        "message":"pong"
    }
    return out

@app.get("/version")
def version():
    out = {
        "status": "ok"
        "version": VERSION,
        "server_time" datetime.now().strftime("%F %H:%M:%S")
    }
    return out