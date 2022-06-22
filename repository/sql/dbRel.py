import sqlite3
from flask import current_app, g

DATABASE = 'repository/sql/database.db'


# Initizalize db and add commands.
def init_app(app):
    app.config['DATABASE'] = DATABASE # add db to configuration
    app.teardown_appcontext(shut_db)


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect( # add database to g scope
            current_app.config['DATABASE'], # read the db from configuration
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def shut_db(e):
    db = g.pop('db', None)
    if db is not None:
        db.close()
