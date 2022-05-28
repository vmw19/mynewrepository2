from flask import (
    Flask,
    request
)
frin datetune import datetime
app = Flak(_name_)


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
        "server_time" datetime.now().strftime("%F %H")
    }