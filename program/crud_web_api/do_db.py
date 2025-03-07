from flask import g
import sqlite3
from constant_global import getDbName
from program.crud_web_api.application import app


# SQLite连接管理
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(getDbName)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
