import os
import base64
import json
from flask import Blueprint, jsonify, request
from app.util.authData import AuthData, saveAuthData, getAuthData
from .config import Config
from .mongo import mongo

# Define a Blueprint for routes
main_blueprint = Blueprint("main", __name__)


def generateBytes(bytesSize: int = 16):
    # Generate 16 random bytes (or however many you need)
    random_bytes = os.urandom(bytesSize)

    # Base64 encode the random bytes
    encoded_bytes = base64.b64encode(random_bytes)

    # Convert to string for easy display (optional)
    return encoded_bytes.decode("utf-8")


def prepareResponse(data: list, status_code: int = 200):
    out = ""
    for e in data:
        out += json.dumps(e) + "\n"
    if Config.IS_CRYPT:
        raise Exception("TODO")
    else:
        
        return out, 200


@main_blueprint.route("/")
def home():
    return jsonify({"message": "Welcome to the Toaru API!"})


@main_blueprint.route("//Auth/gatein.php", methods=["POST"])
def gatein():
    
    data = request.get_json(force=True)  # Get the JSON data
    # You can add validation logic for required fields here
    # if "version" not in data or "cl_ver" not in data:
    #     return jsonify({"error": "Missing 'version' or 'cl_ver' in request data"}), 400

    if data["cl_ver"] != Config.APP_VER:
        return jsonify({"error": "Outdated client"}), 400

    return jsonify(
        {
            "res_code": 0,
            "res_str": "",
            "login_url": Config.LOGIN_URL,
            "resource_url": Config.RES_URL,
            "web_url": Config.WEB_URL,
            "patch_version": Config.RES_VER,
            "native_token": generateBytes(64),
            "smartbeat_enable": Config.SMARTBEAT_ENABLE,
            "cdn_enable": Config.CDN_ENABLE,
            "specialbg_enable": Config.SPECIALBG_ENABLE,
            "titleid": Config.TITLEID,
            "title_background_enable": Config.TITLE_BACKGROUND_ENABLE,
        }
    )


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

    print(data)

    authData = AuthData()
    authData.uuid = uuid
    authData.nativeToken = nativeToken
    authData.nativeSessionId = nativeSessionId
    authData.sessionKey = None
    authData.sharedSecurityKey = sharedSecurityKey
    authData._id = uuid

    saveAuthData(authData)

    return jsonify(
        {
            "nativeSessionId": nativeSessionId,
            "sharedSecurityKey": sharedSecurityKey,
        }
    )


@main_blueprint.route("/Auth/login.php", methods=["POST"])
def login():
    data = request.get_json(force=True)  # Get the JSON data
    # You can add validation logic for required fields here
    # if "version" not in data or "cl_ver" not in data:
    #     return jsonify({"error": "Missing 'version' or 'cl_ver' in request data"}), 400

    uuid = data["uuid"]
    token = data["token"]
    hash_token = data["hash_token"]
    nativeSessionId = data["native_session_id"]

    # Check if data exists
    _data = getAuthData(uuid=uuid, nativeSessionId=nativeSessionId)
    if _data is None:
        return jsonify({"error": "failed to authenticate"}), 401

    nativeSessionId = generateBytes(16)
    sessionKey = generateBytes(16)
    auth_code = generateBytes(10)  # GUID
    # authCode = generateBytes()
    nativeTagName = "apsje0hN7tvrg"
    linkTagName = "lnFsXiEXzUAVDKCZyd"

    _data["nativeSessionId"] = nativeSessionId
    _data["authCode"] = auth_code
    _data["sessionKey"] = sessionKey

    return jsonify(
        {
            "res_code": 0,
            "res_str": "",
            "regist_ok": 1,
            "sess_key": sessionKey,
            "api_url": Config.API_URL,
            "resource_url": Config.RES_URL,
            "web_url": Config.WEB_URL,
            "auth_code": auth_code,
            "auth_code_one_time_key": "",
            "native_tag_name": nativeTagName,
            "link_tag_name": linkTagName,
            "native_session_id": nativeSessionId,
            "patch_version": Config.RES_VER,
            "is_crypt": Config.IS_CRYPT,
            "topic_name": "index-if",
        }
    )


# socialsv components
@main_blueprint.route("/api/Connect", methods=["POST"])
def Connect():

    success = [
        {
            "res_code": 0,
            "res_str": "OK",
            "server_time": 1727283075,
            "session_time": 1727284874,
            "patch_version": 145474,
            "tag_schedule_version": 14200,
        },
        {
            "hand_shake": {"userid": 1587615},
            "do_create_user": 0,
            "tutorial_download_idx": 1,
            "inviteid": 260026556,
        },
    ]

    return prepareResponse(success, 200)

# TODO proper implementation
@main_blueprint.route("/api/GetOnceDiffResultAll2", methods=["POST"])
def GetOnceDiffResultAll2():
    data = json.load(open("./sample/sampleResponseDiff.json", 'r'))
    return prepareResponse(data, 200)

# TODO proper implementation
@main_blueprint.route("/api/GetUser", methods=["POST"])
def GetUser():
    data = json.load(open("./sample/sampleResponseUser.json", 'r'))
    return prepareResponse(data, 200)

# TODO proper implementation
@main_blueprint.route("/api/PurchaseCheck", methods=["POST"])
def PurchaseCheck():
    data = json.load(open("./sample/sampleResponsePurchaseCheck.json", 'r'))
    return prepareResponse(data, 200)

@main_blueprint.route("/api/GetHome2", methods=["POST"])
def GetHome2():
    data = json.load(open("./sample/sampleResponseHome2.json", 'r'))
    return prepareResponse(data, 200)

@main_blueprint.route("/api/GetHome2_2", methods=["POST"])
def GetHome2_2():
    data = json.load(open("./sample/sampleResponseHome2_2.json", 'r'))
    return prepareResponse(data, 200)

@main_blueprint.route("/api/StartStory", methods=["POST"])
def StartStory():
    # ID: 927040001
    data = json.load(open("./sample/sampleResponseStartStory.json", 'r'))
    return prepareResponse(data, 200)

@main_blueprint.route("/web/")
def WebRoot():
    return "HTML missing lmao."

@main_blueprint.route("/api/GetGachaList", methods=["POST"])
def GachaList():
    # ID: 927040001
    data = json.load(open("./sample/sampleResponseGachaList.json", 'r'))
    return prepareResponse(data, 200)