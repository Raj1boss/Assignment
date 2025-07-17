# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 16:38:39 2025

@author: rakumar
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    db.init_app(app)
    jwt.init_app(app)

    from app.routes import task_bp
    from app.auth import auth_bp
    app.register_blueprint(task_bp)
    app.register_blueprint(auth_bp)

    return app