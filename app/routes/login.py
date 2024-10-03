from flask import Blueprint, jsonify, request
from ..config import Config
from ..util.generate import generateBytes
from ..util.authData import getAuthData, saveAuthData

main_blueprint = Blueprint("login", __name__)

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

# {"uuid":"UUID","market":1,"cl_ver":"6.3.0","is_first":0,"native_session_id":"SessionId","terminal_id":""}
@main_blueprint.route("/Auth/getaddlinksession.php", methods=["POST"])
def getaddlinksession():
    return {}

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
    
    saveAuthData(_data)

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