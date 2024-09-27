import requests
import json
import seaes
import time

class ToaruAPI:
    
    headers = {
        "User-Agent": "UnityPlayer/2021.3.9f1 (UnityWebRequest/1.0, libcurl/7.80.0-DEV)",
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded",
        "X-Unity-Version": "2021.3.9f1"
    }
    appVersion = "6.3.0"
    verify = True
    
    def __init__(self, uuid: str, token: str, hash_token: str, isDebug: bool = False) -> None:
        # Urls
        self.gateinUrl = "https://login.index-if.jp//Auth/gatein.php"
        self.loginUrl = ""
        self.sessionUrl = "https://psg.sqex-bridge.jp/native/session"
        self.gameUrl = ""
        self.resUrl = ""
        
        # User data
        self.uuid = uuid
        self.token = token
        self.hash_token = hash_token
        
        # Client data
        self.sessionKey = b''
        self.isCrypt = False
        self.nativeToken = ""
        self.nativeSessionId = "",
        self.sharedSecurityKey = ""
        
        # Res data
        self.patchVersion = 0
        
        # Internal usage data
        self.isInit = False
        self.isDebug = isDebug
        pass
    
    def decodeResponse(self, blobResponse) -> list:
        _resBody = seaes.decrypt(bytearray(blobResponse), bytearray(self.sharedSecurityKey.encode('utf-8'))).decode('utf-8')
        _resBody = _resBody.split('\n')
        out = []
        for e in _resBody:
            out.append(json.loads(e))
        return out
    
    def makeRequest(self, endpoint: str, body: object, method: str = "post") -> object:
        if not self.isInit:
            raise Exception("make login first")
        
        if (body):
            _body = json.dumps(body)
        else:
            _body = None
        _url = self.gameUrl + endpoint
        
        if (self.isCrypt and not _body is None):
            _body = seaes.encrypt(bytearray(_body.encode("utf-8")), bytearray(self.sharedSecurityKey.encode('utf-8')))
            
        if (self.isDebug):
            print(f"Request: {_url} - Crypto?: {self.isCrypt} - {body}")
            
        r = requests.post(_url, data=_body, headers=self.headers, verify=self.verify)
        
        if (self.isDebug):
            if (self.isCrypt):
                _resBody = self.decodeResponse(r.content)
            else:
                _resBody = r.text
            print(f'response: {r.status_code} - {_resBody}')
            open(f'{time.time()}.txt', 'w').write(f'''
Request: {_url}
Request Data: {body}
=====================================
Response: {r.status_code}
Response Data: {_resBody}
''')

        if (self.isCrypt):
            _resBody = self.decodeResponse(r.content)
            # _resBody = _resBody[:-1]
        else:
            _resBody = r.json()
        
        return _resBody
    
    def login(self) -> bool:
        if self.isInit:
            raise Exception("already logged in. dispose the class for loggin in again")
        
        # Stage 1: gatein
        body = {"market":1,"cl_ver":self.appVersion,"review_key":"h4dLNHjEbfw47D"}
        r = requests.post(self.gateinUrl, json=body, headers=self.headers, verify=self.verify)
        if self.isDebug:
            print(f'response: {r.status_code} - {r.text}')
        assert r.status_code == 200, "not 200"
        data = r.json()
        
        self.nativeToken = data['native_token']
        self.loginUrl = data['login_url']
        self.resUrl = data['resource_url']
        
        # Stage 2: session
        body = {
            "UUID": self.uuid,
            "deviceType": 1,
            "nativeToken": self.nativeToken,
            "nativeSessionId": None
        }
        
        r = requests.post(self.sessionUrl, json=body, headers=self.headers, verify=self.verify)
        if self.isDebug:
            print(f'response: {r.status_code} - {r.text}')
        assert r.status_code == 200, "not 200"
        data = r.json()
        
        self.nativeSessionId = data['nativeSessionId']
        self.sharedSecurityKey = data['sharedSecurityKey']
        
        # Stage 3: login
        url = self.loginUrl + "login.php"
        body = {
            "id": "",
            "pw": "",
            "auth_code": self.uuid,
            "os": 0,
            "carrier": 0,
            "market": 1,
            "lang": 0,
            "uuid": self.uuid,
            "device": "iPhone16,1",
            "token": self.token,
            "cl_ver": "6.3.0",
            "os_ver": "iOS 18.1",
            "hash_token": self.hash_token,
            "is_first": 0,
            "native_session_id": self.nativeSessionId,
            "terminal_id": "E8EE19D7-7EB3-4CA8-A2D4-5999BDBCD66E",
            "is_tracking_enabled": 0,
            "advertising_id": "00000000-0000-0000-0000-000000000000"
        }
        
        r = requests.post(url, json=body, headers=self.headers, verify=self.verify)
        if self.isDebug:
            print(f'response: {r.status_code} - {r.text}')
        assert r.status_code == 200, "not 200"
        data = r.json()
        
        self.sessionKey = data['sess_key']
        self.isCrypt = data['is_crypt']
        self.patchVersion = data['patch_version']
        self.authCode = data['auth_code']
        self.resUrl = data['resource_url']
        self.gameUrl = data['api_url']
        
        self.headers["Cookie"] = "sk=%s;cv=0;rc=1" % self.sessionKey
        
        self.isInit = True
        
        return True
    
    
if __name__ == "__main__":
    api = ToaruAPI(
        "00d97bdd-ef93-4e93-b515-62260e902ab1", 
        "dllWmm-WgkC7oGlLugxwZq:APA91bGblIYGmqHW8fVs36HtVyGKRee0m4KJQlcDYFvfYNAXdpDzqylWpKchcYcOzfY3KFLgTB-E0xhmVWxNPbHrODBecaWKFTxxp0R4-c3JpT8Yh6GxNew91Y6un-PKxySVs16G_9Kh", 
        "JwmKO/hANjxrGx5PfsOaSL+aAgI=", 
        isDebug=False
    )
    api.login()
    print("login done!")
    data = api.makeRequest("Connect", None)
    # data = api.makeRequest("GetOnceDiffResultAll2", {"idx":0})
    # data = api.makeRequest("GetUser", None)
    # data = api.makeRequest("PurchaseCheck", None)
    # data = api.makeRequest("GetHome2", {"is_logined_first":[1]})
    # data = api.makeRequest("StartStory", {"storyid":927040001,"select_deckid":4,"guest_userid":0})
    data = api.makeRequest("GetGachaList", None)
    json.dump(data, open("data.json", "w"))