from flask import Flask
from dotenv import load_dotenv
import os

from app.extensions import db, login_manager, csrf, mail

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "devsecretkey")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hyde.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions with app
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    mail.init_app(app)

    from app.auth.routes import auth
    app.register_blueprint(auth)

    return app
