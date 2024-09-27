class Config:
    SECRET_KEY = 'your_secret_key_here'
    DEBUG = True
    MONGO_URI = 'mongodb://localhost:27017/ToaruIF'  # Update with your MongoDB URI
    
    # ToaruIF Client Data
    RES_VER = 145545
    APP_VER = "6.3.0"
    CDN_ENABLE = 1
    SPECIALBG_ENABLE = 0
    TITLEID = 0
    TITLE_BACKGROUND_ENABLE = 1
    SMARTBEAT_ENABLE = 0
    LOGIN_URL = "https://192.168.1.179:40443/Auth/"
    RES_URL = "http://cache.index-if.jp/ver2/" # "https://192.168.1.179:40443/ver2/"
    WEB_URL = "https://192.168.1.179:40443/web/"
    API_URL = "https://192.168.1.179:40443/api/"
    
    # ToaruIF Server Config
    IS_CRYPT = 0 # 0 is sending JSON, 1 is sending encrypted data
    
    # ToaruIF Server constants
    GAME_CONSTS = {} # TODO import