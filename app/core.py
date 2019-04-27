from flask import Flask
from config import Config
from extensions import db, migrate
from app import models

from app.main import routes as main


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    main.configure(app)

    return app
