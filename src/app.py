from flask import Flask
from flask_cors import CORS

import src.config as config
from src.extensions.db import db, migrate

app = Flask(__name__)
app.config.from_object(config)
app.debug = config.DEBUG

db.init_app(app)
migrate.init_app(app, db)

db.app = app


CORS(
    app,
    resources={r"/*": {"origins": "*"}},
    headers=['Content-Type', 'X-Requested-With', 'Authorization']
)

from .helloWorld import hello_world_blueprint
app.register_blueprint(hello_world_blueprint)


if __name__ == '__main__':
    app.run(host=config.HOST, port=config.PORT)