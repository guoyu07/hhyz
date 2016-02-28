from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.mail import Mail
from flask.ext.login import LoginManager
from .filter import format_date,slug,is_collect
from config import config

db=SQLAlchemy()
mail=Mail()
login_manager=LoginManager()
login_manager.login_view='auth.login_view'
login_manager.session_protection='strong'

def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    mail.init_app(app)
    login_manager.init_app(app)
    db.init_app(app)
    from api import api as api_blueprint
    app.register_blueprint(api_blueprint,url_prefix='/api')

    from auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/auth')

    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    app.jinja_env.filters['format_date']=format_date
    app.jinja_env.filters['slug']=slug
    app.jinja_env.filters['is_collect']=is_collect
    return app

