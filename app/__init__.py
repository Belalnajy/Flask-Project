from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config
from sqlalchemy.orm import DeclarativeBase
from flask_login import LoginManager
from flask import render_template

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = "auth.login"


class Base(DeclarativeBase):
    pass

db=SQLAlchemy(model_class=Base)

def create_app(environment):
    # app = Flask(__name__,template_folder='./templates')
    app = Flask(__name__)  
    app.config.from_object(config.get(environment or "development"))

    # Initialize SQLAlchemy and Flask-Migrate extensions.
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    # Register Blueprints
    register_blueprints(app)
    @app.errorhandler(403)
    def forbidden_error(error):
        return render_template('errors/403.html'), 403
    # Create database tables if they don't exist already.
    with app.app_context():
        db.create_all()

    return app

def register_blueprints(application):
    # Blueprints are registered here.
    from app.main.routes import main as main_blueprint
    from app.auth.routes import auth as auth_blueprint
    application.register_blueprint(main_blueprint)
    application.register_blueprint(auth_blueprint)
    