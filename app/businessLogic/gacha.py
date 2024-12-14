import json
import random

from ..util.add import (
    addAssistCard,
    addBattleCard,
    COLLECTION_NAME_GACHA_STATUS,
)
from ..util.importData import BATTLE_CARD_DATA, ASSIST_CARD_DATA


def GetGachaList() -> list:
    return


def ExecuteGacha2(
    userId: int,
    gachaId: int,
    gachaPayTypeId: int,
    playIndex: int,
    execNum: int,
    isTutorial: bool = False,
):

    if isTutorial:
        data = json.load(open("data/GachaTutorialList.json", "r"))
    else:
        data = json.load(open("data/GachaList.json", "r"))

    gachaData = [e for e in data if e["gacha_base"]["gachaid"] == gachaId][0]
    gachaPaymentInfo = gachaData["play_infos"][playIndex]

    # CardObtainType:
    # 0 = Permanent
    # 1 = ImaFes
    # 2 = Seasonal (limited)
    # 3 = Event (non-gacha)
    # 4 = Memorial (limited-time login?)
    # 5 = Shop-Limited
    # 6 = Collabo
    if isTutorial:
        obtainTypeFilter = [0]
    else:
        obtainTypeFilter = [0, 1, 2, 6]

    possibleIds = [
        (obj["key"], obj["rarity"], "battle")
        for obj in BATTLE_CARD_DATA
        if obj["obtain"] in obtainTypeFilter and obj["rarity"] > 2
    ]
    possibleIds += [
        (obj["key"], obj["rarity"], "assist")
        for obj in ASSIST_CARD_DATA
        if obj["obtain"] in obtainTypeFilter and obj["rarity"] > 2
    ]

    isRarityGuaranteeObtained = False
    playTimes = gachaPaymentInfo["lot_num"]
    results = []

    for i in range(0, playTimes):
        isOk = False
        while not isOk:
            r = random.choice(possibleIds)
            if playTimes > 1 and (
                i == playTimes - 1 and not isRarityGuaranteeObtained
            ):
                continue
            isOk = True
        if playTimes == 1 or r[1] > 2:
            isRarityGuaranteeObtained = True
        if r[2] == "battle":
            addBattleCard(userId, r[0])
        else:
            addAssistCard(userId, r[0])
        results.append(
            {
                "group": 0,
                "rate": 0,
                "rate2": 0,
                "type": 10,
                "id": 120001001,
                "num": 1,
                "max": 0,
                "param1": r[0],
                "param2": 0,
                "param3": 0,
                "rarity": 0,
            }
        )
        i += 1

    return results
