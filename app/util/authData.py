import json
from ..mongo import mongo, get_next_sequence_value

class AuthData:
    _id: str
    userId: int
    uuid: str
    nativeToken: str
    nativeSessionId: str
    sharedSecurityKey: str
    sessionKey: str
    hashToken: str = None
    authCode: str = None

def saveAuthData(data: AuthData):
    try:
        _data = getAuthData(uuid=data["uuid"])
    except TypeError:
        _data = getAuthData(uuid=data.uuid)
    try:
        data = data.__dict__
    except AttributeError:
        pass
    except TypeError:
        pass
    
    # print(_data)
    if _data:
        mongo.db.auth_data.replace_one(
            {"uuid": data['uuid']},
            data,
        )
    else:
        data["userId"] = get_next_sequence_value("USER_ID")
        mongo.db.auth_data.insert_one(
            data
        )
    
def getAuthData(uuid: str = None, nativeToken: str = "", nativeSessionId: str = "", sessionKey: str = "") -> AuthData:
    
    filter = {}
    if uuid:
        filter['uuid'] = uuid
    if nativeToken:
        filter['nativeToken'] = nativeToken
    if nativeSessionId:
        filter['nativeSessionId'] = nativeSessionId
    if sessionKey:
        filter['sessionKey'] = sessionKey
    
    return mongo.db.auth_data.find_one(filter)
