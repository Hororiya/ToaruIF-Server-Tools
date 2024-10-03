from flask import Blueprint, jsonify, request
from ..util.generate import generateBytes
from ..util.authData import *

main_blueprint = Blueprint("square", __name__)

@main_blueprint.route("/native/session", methods=["POST"])
def session():
    data = request.get_json(force=True)  # Get the JSON data
    # You can add validation logic for required fields here
    # if "name" not in data or "value" not in data:
    #     return jsonify({"error": "Missing 'name' or 'value' in request data"}), 400

    uuid = data["UUID"]
    nativeToken = data["nativeToken"]
    nativeSessionId = generateBytes(16)
    sharedSecurityKey = generateBytes(16)

    data = mongo.db.auth_data.find_one({"uuid": uuid})

    # print(data)

    authData = AuthData()
    authData.uuid = uuid
    authData.nativeToken = nativeToken
    authData.nativeSessionId = nativeSessionId
    authData.sessionKey = None
    authData.sharedSecurityKey = sharedSecurityKey
    authData.userId = 0 if data is None else data["userId"]
    authData._id = uuid

    saveAuthData(authData)

    return jsonify(
        {
            "nativeSessionId": nativeSessionId,
            "sharedSecurityKey": sharedSecurityKey,
        }
    )

