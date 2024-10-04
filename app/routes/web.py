from flask import Blueprint
from ..util.authData import *

main_blueprint = Blueprint("web", __name__)

@main_blueprint.route("/web/")
def WebRoot():
    return "HTML missing lmao."