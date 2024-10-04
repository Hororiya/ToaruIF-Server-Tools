from flask import Blueprint, jsonify
from app.routes.api import main_blueprint as api_blueprint
from app.routes.login import main_blueprint as login_blueprint
from app.routes.squareSession import main_blueprint as square_blueprint
from app.routes.web import main_blueprint as web_blueprint

# Define a Blueprint for routes
main_blueprint = Blueprint("main", __name__)

@main_blueprint.route("/")
def home():
    return jsonify({
        "message": "Welcome to the Toaru API!",
        # "availableEndpoints": main_blueprint.__dict__
        })

def register_blueprints(app):
    # Register blueprints here
    app.register_blueprint(api_blueprint)
    app.register_blueprint(login_blueprint)
    app.register_blueprint(square_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(web_blueprint)