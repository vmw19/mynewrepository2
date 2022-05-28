from flask import (
    Flask,
    request
)

app = Flak(_name_)


@app.get('/ping')
def poing():
    out = {
        "status": "ok",
        "message":"pong"
    }
    return out, 200