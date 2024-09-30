import json
from time import time
from ..mongo import mongo
from ..config import Config

COLLECTION_NAME = "DecorationInfo"

def getDecorationInfo(userId: int) -> list:
    # TODO get from DB (collection DecorationInfo)
    return [
        {"content_type": 28, "param": 100090019, "sp_badgeid": 2},
        {"content_type": 25, "param": 2500, "sp_badgeid": 2500},
        {"content_type": 28, "param": 100090015, "sp_badgeid": 2},
        {"content_type": 28, "param": 100090017, "sp_badgeid": 2},
        {"content_type": 28, "param": 100090018, "sp_badgeid": 2},
    ]
    
def saveDecorationInfo(userId: int, decorationData: list) -> bool:
    data = mongo.db[COLLECTION_NAME].find_one({"userId": userId})
    obj = {
        "_id": userId,
        "userId": userId,
        "decorationData": decorationData
    }
    
    if data:
        mongo.db[COLLECTION_NAME].replace_one({"userId": userId}, decorationData)
    else:
        mongo.db[COLLECTION_NAME].insert_one(obj)
    
    return True


def getMainResponseData(userId: int, isOk: bool = True) -> object:
    # TODO error
    return {
        "res_code": 0,
        "res_str": "OK",
        "server_time": int(time()),
        "session_time": int(time()),
        "patch_version": Config.RES_VER,
        "tag_schedule_version": 14200,
        "menu_decoration_infos": getDecorationInfo(userId),
        "is_update_menu_decoration": [1],
    }
