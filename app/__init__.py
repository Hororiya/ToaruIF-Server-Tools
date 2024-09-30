from flask import Flask
from flask_talisman import Talisman
from .mongo import init_mongo
from .routes import register_blueprints
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Enforce HTTPS
    Talisman(app)
    
    # Initialize MongoDB
    init_mongo(app)
    
    # Register Blueprints
    register_blueprints(app)

    return app