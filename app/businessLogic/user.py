from ..mongo import mongo
from ..util.add import (
    COLLECTION_NAME_USER,
    COLLECTION_NAME_USER_LOGIN_DATA,
    addAssistCard,
    addBattleCard,
    addUser,
    COLLECTION_NAME_USER_STATUS,
    addUserTitle,
    addUserMoney,
    addUserStatus,
    setDecorations
)
from .deck import generateDeckData
from .card import BATTLE_CARD_DATA, ASSIST_CARD_DATA
from ..config import Config


def getUserStatusData(userId: int) -> list:
    data = mongo.db[COLLECTION_NAME_USER_STATUS].find_one({"user_owner_id": userId})
    del data["_id"]
    del data["user_owner_id"]
    return [data]


def getUserStamps(userId: int) -> list:
    # TODO proper logic
    out = []
    for i in range(1, 8):
        out.append({"stampid": i})
    return out


def getUserTutorial(userId: int) -> list:
    data = mongo.db[COLLECTION_NAME_USER_LOGIN_DATA].find_one({"userId": userId})
    return [
        {
            "complete_flag": data["tutorialStatus"],
            "play_tutorial_type": data["tutorialType"],
            "play_tutorial_idx": data["tutorialIndex"],
            "prologue_finish_time": data["tutorialClearDate"],
        }
    ]


def saveUserTutorialStatus(userId: int, tutorialType: int, tutorialIdx: int):
    mongo.db[COLLECTION_NAME_USER_LOGIN_DATA].update_one(
        {"userId": userId},
        {"$set": {"tutorialType": tutorialType, "tutorialIndex": tutorialIdx}},
    )


def clearUserTutorialStatus(userId: int):
    mongo.db[COLLECTION_NAME_USER_LOGIN_DATA].update_one(
        {"userId": userId},
        {
            "$set": {
                "tutorialStatus": 1,
                "tutorialType": 0,
                "tutorialIndex": 0,
                "tutorialClearDate": "2024-01-01 00:00:00",
            }
        },
    )


def getUserMoney(userId: int) -> list:
    # TODO proper logic
    return [
        {"type": 2, "param": 0, "num": 44280},
        {"type": 3, "param": 0, "num": 402219},
        {"type": 4, "param": 0, "num": 1290},
        {"type": 5, "param": 0, "num": 278},
        {"type": 6, "param": 0, "num": 460},
        {"type": 20, "param": 15, "num": 600},
        {"type": 20, "param": 25, "num": 0},
        {"type": 20, "param": 34, "num": 0},
        {"type": 20, "param": 38, "num": 60},
        {"type": 20, "param": 39, "num": 0},
        {"type": 20, "param": 40, "num": 0},
        {"type": 20, "param": 45, "num": 0},
        {"type": 20, "param": 48, "num": 0},
        {"type": 20, "param": 54, "num": 140},
        {"type": 20, "param": 57, "num": 110},
        {"type": 20, "param": 60, "num": 480},
        {"type": 20, "param": 66, "num": 20},
        {"type": 20, "param": 78, "num": 32},
        {"type": 20, "param": 82, "num": 0},
        {"type": 20, "param": 98, "num": 30},
        {"type": 20, "param": 504, "num": 0},
        {"type": 20, "param": 505, "num": 0},
        {"type": 20, "param": 509, "num": 0},
        {"type": 20, "param": 510, "num": 0},
        {"type": 20, "param": 511, "num": 100},
        {"type": 20, "param": 515, "num": 0},
        {"type": 20, "param": 516, "num": 0},
        {"type": 20, "param": 517, "num": 0},
        {"type": 20, "param": 518, "num": 0},
        {"type": 20, "param": 5007, "num": 20},
        {"type": 20, "param": 5018, "num": 29},
        {"type": 20, "param": 5020, "num": 30},
        {"type": 20, "param": 5028, "num": 110},
        {"type": 20, "param": 5031, "num": 30},
        {"type": 20, "param": 5032, "num": 20},
        {"type": 20, "param": 5043, "num": 20},
        {"type": 20, "param": 5058, "num": 0},
        {"type": 20, "param": 6402, "num": 0},
        {"type": 20, "param": 6403, "num": 0},
        {"type": 21, "param": 7, "num": 60},
        {"type": 21, "param": 25, "num": 16},
        {"type": 21, "param": 34, "num": 27},
        {"type": 21, "param": 38, "num": 0},
        {"type": 21, "param": 39, "num": 4},
        {"type": 21, "param": 40, "num": 19},
        {"type": 21, "param": 45, "num": 3},
        {"type": 21, "param": 48, "num": 89},
        {"type": 21, "param": 54, "num": 26},
        {"type": 21, "param": 57, "num": 287},
        {"type": 21, "param": 58, "num": 279},
        {"type": 21, "param": 60, "num": 6},
        {"type": 21, "param": 66, "num": 290},
        {"type": 21, "param": 76, "num": 492},
        {"type": 21, "param": 78, "num": 18},
        {"type": 21, "param": 82, "num": 136},
        {"type": 21, "param": 90, "num": 300},
        {"type": 21, "param": 92, "num": 549},
        {"type": 21, "param": 98, "num": 13},
        {"type": 21, "param": 5007, "num": 16},
        {"type": 21, "param": 5018, "num": 24},
        {"type": 21, "param": 5020, "num": 48},
        {"type": 21, "param": 5028, "num": 459},
        {"type": 21, "param": 5031, "num": 18},
        {"type": 21, "param": 5032, "num": 12},
        {"type": 21, "param": 5043, "num": 24},
        {"type": 21, "param": 5050, "num": 678},
        {"type": 21, "param": 5052, "num": 165},
        {"type": 21, "param": 5058, "num": 20},
        {"type": 25, "param": 30, "num": 20375},
        {"type": 25, "param": 33, "num": 5310},
        {"type": 25, "param": 47, "num": 13342},
        {"type": 25, "param": 59, "num": 5644},
        {"type": 25, "param": 83, "num": 8465},
        {"type": 26, "param": 30, "num": 9900},
        {"type": 26, "param": 33, "num": 4890},
        {"type": 26, "param": 59, "num": 1980},
        {"type": 26, "param": 83, "num": 1170},
        {"type": 30, "param": 0, "num": 249796},
        {"type": 31, "param": 0, "num": 24626},
        {"type": 32, "param": 0, "num": 68},
        {"type": 33, "param": 0, "num": 62},
        {"type": 36, "param": 1005, "num": 140},
        {"type": 36, "param": 1017, "num": 320},
        {"type": 36, "param": 1500, "num": 350},
        {"type": 37, "param": 0, "num": 125},
        {"type": 40, "param": 2000, "num": 0},
        {"type": 40, "param": 2001, "num": 0},
        {"type": 40, "param": 2002, "num": 0},
        {"type": 40, "param": 2003, "num": 14},
        {"type": 40, "param": 2004, "num": 0},
        {"type": 40, "param": 2005, "num": 19},
        {"type": 40, "param": 2007, "num": 4},
        {"type": 41, "param": 280002, "num": 14230},
        {"type": 41, "param": 280102, "num": 9770},
        {"type": 41, "param": 280202, "num": 400},
        {"type": 41, "param": 280302, "num": 2730},
        {"type": 42, "param": 0, "num": 120},
        {"type": 43, "param": 47, "num": 44},
        {"type": 43, "param": 49, "num": 788},
        {"type": 43, "param": 59, "num": 200},
        {"type": 43, "param": 63, "num": 860},
        {"type": 43, "param": 83, "num": 80},
        {"type": 44, "param": 47, "num": 16},
        {"type": 44, "param": 49, "num": 10},
        {"type": 44, "param": 59, "num": 8},
        {"type": 44, "param": 63, "num": 9},
        {"type": 44, "param": 83, "num": 17},
        {"type": 45, "param": 2500, "num": 370},
        {"type": 45, "param": 2501, "num": 30},
        {"type": 45, "param": 2504, "num": 180},
        {"type": 45, "param": 2505, "num": 80},
        {"type": 45, "param": 2508, "num": 20},
        {"type": 45, "param": 2516, "num": 270},
        {"type": 45, "param": 2528, "num": 40},
        {"type": 47, "param": 0, "num": 0},
        {"type": 47, "param": 160012002, "num": 1000},
        {"type": 55, "param": 0, "num": 470},
        {"type": 59, "param": 6401, "num": 270},
        {"type": 59, "param": 6402, "num": 8},
        {"type": 59, "param": 6403, "num": 30},
        {"type": 59, "param": 6507, "num": 30},
        {"type": 60, "param": 2100, "num": 10},
        {"type": 45, "param": 2546, "num": 10},
        {"type": 1, "param": 0, "num": 99999999999},
    ]


def getUserTitle(userId: int) -> list:
    # TODO proper logic
    return [
        {
            "user_titleid": 30011000,
            "user_title_param": 0,
            "state": 2,
            "received_time": 1594286474,
        }
    ]


def getUserCostume(userId: int) -> list:
    # TODO proper logic
    return [{"costumeid": 1000201, "flag": 4}]


def getUserData(userId: int) -> list:
    data = mongo.db[COLLECTION_NAME_USER].find_one({"userid": userId})
    del data["_id"]
    return [data]


def changeName(userId: int, name: str) -> object:
    mongo.db[COLLECTION_NAME_USER].update_one(
        {"userid": userId}, {"$set": {"name": name}}
    )
    data = mongo.db[COLLECTION_NAME_USER].find_one({"userid": userId})
    del data["_id"]
    return [data]


def createUser(userId: int) -> bool:
    # Add User on mongodb
    addUser(userId)
    addUserStatus(userId)

    if Config.CREATE_WITH_EVERYTHING: # Cheat creation
        # Add assist cards
        for card in ASSIST_CARD_DATA:
            addAssistCard(userId, card["key"])
        
        i = 0
        # Add battle cards
        for card in BATTLE_CARD_DATA:
            if i == 0:
                data = addBattleCard(userId, card["key"])
                i+=1
            else:
                addBattleCard(userId, card["key"])
        pass
    else: # Legit creation
        # Add battle cards
        data = addBattleCard(userId, 100111001)
        addBattleCard(userId, 100412001)

        # Add assist cards
        addAssistCard(userId, 200212001)

    # Add decorations
    setDecorations(userId, [{"content_type":10,"param":601,"sp_badgeid":300000002},{"content_type":25,"param":2500,"sp_badgeid":2500}])

    # Add decks
    generateDeckData(userId, data["battle_card_uniqid"])

    # Add user titles
    addUserTitle(userId, 70031001)

    # Add user money
    addUserMoney(userId, type=1, param=0, num=250)

    return True
