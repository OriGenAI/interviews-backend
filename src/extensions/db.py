from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa
from flask_migrate import Migrate
from sqlite3 import Connection as sqlite_connection
import re

db = SQLAlchemy()


def _regexp(expr, item):
    reg = re.compile(expr, re.I)
    return reg.search(item) is not None


@sa.event.listens_for(sa.engine.Engine, "connect")
def sqlite_engine_connect(dbapi_conn, connection_record):
    if isinstance(dbapi_conn, sqlite_connection):
        dbapi_conn.create_function("regexp", 2, _regexp)


migrate = Migrate()