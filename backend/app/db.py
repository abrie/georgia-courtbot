import sqlite3
import spatialite

from flask import current_app, g


def get_db():
    if "db" not in g:
        g.cbp_db = sqlite3.connect(
            current_app.config["DATABASE"], detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.cbp_db.text_factory = lambda b: b.decode(errors="ignore")
        g.cbp_db.row_factory = sqlite3.Row

    return g.cbp_db


def close_dbs():
    db = g.pop("db", None)

    if db is not None:
        db.close()


def init_app(app):
    app.teardown_appcontext(close_dbs)
