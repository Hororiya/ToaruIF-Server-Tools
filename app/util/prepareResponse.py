import json
from ..config import Config


def prepareResponse(data: list, status_code: int = 200):
    out = ""
    for e in data:
        out += json.dumps(e) + "\n"
    if Config.IS_CRYPT:
        raise Exception("TODO")
    else:
        
        return out, 200