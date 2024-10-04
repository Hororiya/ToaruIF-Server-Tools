import json
from time import time
from ..mongo import mongo
from ..config import Config
from .add import COLLECTION_NAME_MENU_DECORATION_INFOS, setDecorations


def getDecorationInfo(userId: int) -> list:
    # TODO get from DB (collection DecorationInfo)
    out = [
        {"content_type": 10, "param": 601, "sp_badgeid": 300000002},
        {"content_type": 25, "param": 2500, "sp_badgeid": 2500},
    ]
    data = mongo.db[COLLECTION_NAME_MENU_DECORATION_INFOS].find_one(
        {"user_owner_id": userId}
    )
    if data:
        out = data["decorations"]
    return out


def saveDecorationInfo(userId: int, decorationData: list) -> bool:
    setDecorations(userId, decorationData)
    return True


def getMainResponseData(userId: int, isOk: bool = True, isReturnHome: bool = False) -> object:
    # TODO error

    res = {
        "res_code": 0,
        "res_str": "OK",
        "server_time": int(time()),
        "session_time": int(time()),
        "patch_version": Config.RES_VER,
        "tag_schedule_version": Config.TAG_SCHEDULE,
        "menu_decoration_infos": getDecorationInfo(userId),
        "is_update_menu_decoration": [1],
    }
    
    if isReturnHome:
        pass

    return res
