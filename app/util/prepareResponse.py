import json
from ..config import Config
from flask import request, Response

def prepareResponse(data: list, status_code: int = 200):
    
    token = request.cookies.get('sk')
    
    out = ""
    for e in data:
        out += json.dumps(e) + "\n"
    if Config.IS_CRYPT:
        raise Exception("TODO")
    else:
        return Response(out, 200, headers={
            "Set-Cookie": f"sk={token}"
        })