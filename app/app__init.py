from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_mail import Mail
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize extensions (but don't tie them to app yet)
db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "devsecretkey")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hyde.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    mail.init_app(app)

    from app.auth.routes import auth
    app.register_blueprint(auth)

    return app

