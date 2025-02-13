from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import Config

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)

    from app.models import User, Task

    from app.auth import auth
    from app.routes import routes

    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(routes, url_prefix="/api")

    return app 
