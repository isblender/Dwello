from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from .api.user_routes import user_blueprint
    from .api.apartment_routes import apartment_blueprint
    from .api.msg_routes import msg_blueprint

    app.register_blueprint(user_blueprint, url_prefix='/api/users')
    app.register_blueprint(apartment_blueprint, url_prefix='/api/apartments')
    app.register_blueprint(msg_blueprint, url_prefix='/api/msgs')

    return app
