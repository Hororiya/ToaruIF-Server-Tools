import json
from ..mongo import mongo

class AuthData:
    _id: str
    userId: int = 0
    uuid: str
    nativeToken: str
    nativeSessionId: str
    sharedSecurityKey: str
    sessionKey: str
    hashToken: str = None
    authCode: str = None

def saveAuthData(data: AuthData):
    _data = getAuthData(uuid=data.uuid)
    data = data.__dict__
    
    print(_data)
    if _data:
        mongo.db.auth_data.replace_one(
            {"uuid": data['uuid']},
            data,
        )
    else:
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
