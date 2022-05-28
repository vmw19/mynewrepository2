from flask import g
import sqlite3

DATABASE_URL = "user_crud.db"

def get_user_by_id