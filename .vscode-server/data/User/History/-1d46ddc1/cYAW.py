from flask import (
    Flask,
    request
)

from datetime import datetime
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

@app.get("/users")
def get_all_users():
    user_list = user.scan()
    out = {
        "status": "ok",
        "users": user_list
    }

    return out

@app.get("/users/<int:pk>")
def get_user_by_id(pk):
    record = user.select_by_id(pk)