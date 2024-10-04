import json
from ..mongo import mongo
from ..util.add import COLLECTION_NAME_BATTLE_CARDS, COLLECTION_NAME_ASSIST_CARDS

ASSIST_CARD_DATA = json.load(open("./data/AssistCard.json", "r"))["items"]
BATTLE_CARD_DATA = json.load(open("./data/BattleCard.json", "r"))["items"]


def getAssistCardsData(userId: int) -> list:
    out = []
    data = mongo.db[COLLECTION_NAME_ASSIST_CARDS].find({"user_owner_id": userId})
    for card in list(data):
        del card["_id"]
        del card["user_owner_id"]
        out.append(card)

    return out


def getBattleCardsData(userId: int) -> list:
    out = []
    data = mongo.db[COLLECTION_NAME_BATTLE_CARDS].find({"user_owner_id": userId})
    for card in data:
        del card["_id"]
        del card["user_owner_id"]
        out.append(card)

    return out
