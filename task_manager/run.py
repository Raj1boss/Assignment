# -*- coding: utf-8 -*-
"""
Created on Thu Jul 17 16:46:57 2025

@author: rakumar
"""

from app import create_app, db
from flask_swagger_ui import get_swaggerui_blueprint

app = create_app()

SWAGGER_URL = "/docs"
API_URL = "/static/swagger.json"
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)