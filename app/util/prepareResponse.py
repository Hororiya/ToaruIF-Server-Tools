import json
from ..config import Config
from flask import request, Response
from lib.toaruIF.seaes import encrypt, decrypt
from .authData import getAuthData

def getRequestData() -> (object, int):
    out = {}
    # Token check
    token = request.cookies.get("sk")
    if not token:
        raise Exception("token missing.")
    # Data and management
    data = getAuthData(sessionKey=token)
    if Config.IS_CRYPT:
        key = bytearray(data['sharedSecurityKey'].encode('utf-8'))
        req = request.get_data()
        if req.__len__() > 0:
            out = decrypt(req, key)
            out = json.loads(out)
        else:
            out = {}
    else:
        req = request.get_data()
        if req.__len__() > 0:
            out = json.loads(req)
    return out, data["userId"]

def prepareResponse(data: list, status_code: int = 200):
    token = request.cookies.get("sk")
    out = ""
    for e in data:
        out += json.dumps(e) + "\n"
    if Config.IS_CRYPT:
        data = getAuthData(sessionKey=token)
        key = bytearray(data['sharedSecurityKey'].encode('utf-8'))
        res = bytearray(out.encode('utf-8'))
        out = encrypt(res, key)
        out = bytes(out)
    return Response(out, status=status_code, headers={"Set-Cookie": f"sk={token}", "X-Crypto-Enabled": Config.IS_CRYPT})
