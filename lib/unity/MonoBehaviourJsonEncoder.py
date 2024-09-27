import UnityPy

def isJsonValue(json_value):
    _type = type(json_value)
    return _type is int or _type is str or _type is float or _type is object or _type is list

def MonoBehaviourJsonEncoder(json_object):
    if type(json_object) == UnityPy.classes.PPtr:
        out = {}
        for key in json_object.__dict__:
            value = json_object.__dict__[key]
            if isJsonValue(value):
                out[key] = value
        return out
    else:
        return json_object