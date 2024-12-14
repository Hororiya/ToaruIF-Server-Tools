from ..mongo import mongo
from ..util.add import COLLECTION_NAME_DECKS


def getDeckTrinityType(userId: int) -> list:
    # TODO logic
    return [
        {"deck_trinity_type": 1, "select_deckid": 1},
        {"deck_trinity_type": 2, "select_deckid": 1},
        {"deck_trinity_type": 3, "select_deckid": 1},
        {"deck_trinity_type": 5, "select_deckid": 1},
        {"deck_trinity_type": 6, "select_deckid": 1},
    ]


# Deck Type:
# 0 : None
# 1 : Story
# 2 : ArenaDefence
# 3 : ArenaAttack
# 4 : EventRaid
# 5 : EventRaidRescue
# 6 : EventGuildBattleRaid
# 7 : EventStory
# 8 : Quest
# 9 : RecaptureBattle
# 10 : ArenaClassTrinityDefence
# 11 : ArenaClassTrinityAttack
# 12 : RecaptureBattleNormal
# 13 : RecaptureBattleHard
# 14 : Trial
def getDeckType(userId: int) -> list:
    return [
        {"deck_type": 1, "select_deckid": 1},
        {"deck_type": 2, "select_deckid": 1},
        {"deck_type": 3, "select_deckid": 2},
        {"deck_type": 4, "select_deckid": 1},
        {"deck_type": 5, "select_deckid": 1},
        {"deck_type": 7, "select_deckid": 2},
        {"deck_type": 8, "select_deckid": 1},
        {"deck_type": 14, "select_deckid": 1},
    ]


def getDeckInfo(userId: int) -> list:
    out = []
    data = mongo.db[COLLECTION_NAME_DECKS].find({"user_id_owner": userId})

    for deck in data:
        del deck["_id"]
        del deck["user_id_owner"]
        out.append(deck)

    return out


def getDeckTrinityInfo(userId: int) -> list:
    # TODO logic
    return [
        {
            "deck_trinity_type": 1,
            "deckid": 1,
            "name": "マイチーム1",
            "battle_card_uniqids_1st1": 0,
            "battle_card_uniqids_1st2": 0,
            "battle_card_uniqids_1st3": 0,
            "battle_card_uniqids_1st4": 0,
            "battle_card_uniqids_1st5": 0,
            "battle_card_uniqids_1st6": 0,
            "assist_card_uniqids_1st1": 0,
            "assist_card_uniqids_1st2": 0,
            "assist_card_uniqids_1st3": 0,
            "assist_card_uniqids_1st4": 0,
            "assist_card_uniqids_1st5": 0,
            "assist_card_uniqids_1st6": 0,
            "battle_card_uniqids_2nd1": 0,
            "battle_card_uniqids_2nd2": 0,
            "battle_card_uniqids_2nd3": 0,
            "battle_card_uniqids_2nd4": 0,
            "battle_card_uniqids_2nd5": 0,
            "battle_card_uniqids_2nd6": 0,
            "assist_card_uniqids_2nd1": 0,
            "assist_card_uniqids_2nd2": 0,
            "assist_card_uniqids_2nd3": 0,
            "assist_card_uniqids_2nd4": 0,
            "assist_card_uniqids_2nd5": 0,
            "assist_card_uniqids_2nd6": 0,
            "battle_card_uniqids_3rd1": 0,
            "battle_card_uniqids_3rd2": 0,
            "battle_card_uniqids_3rd3": 0,
            "battle_card_uniqids_3rd4": 0,
            "battle_card_uniqids_3rd5": 0,
            "battle_card_uniqids_3rd6": 0,
            "assist_card_uniqids_3rd1": 0,
            "assist_card_uniqids_3rd2": 0,
            "assist_card_uniqids_3rd3": 0,
            "assist_card_uniqids_3rd4": 0,
            "assist_card_uniqids_3rd5": 0,
            "assist_card_uniqids_3rd6": 0,
            "select_deck_idx": [0],
            "keeps": [{}, {}, {}],
        },
        {
            "deck_trinity_type": 2,
            "deckid": 1,
            "name": "マイチーム1",
            "battle_card_uniqids_1st1": 0,
            "battle_card_uniqids_1st2": 0,
            "battle_card_uniqids_1st3": 0,
            "battle_card_uniqids_1st4": 0,
            "battle_card_uniqids_1st5": 0,
            "battle_card_uniqids_1st6": 0,
            "assist_card_uniqids_1st1": 0,
            "assist_card_uniqids_1st2": 0,
            "assist_card_uniqids_1st3": 0,
            "assist_card_uniqids_1st4": 0,
            "assist_card_uniqids_1st5": 0,
            "assist_card_uniqids_1st6": 0,
            "battle_card_uniqids_2nd1": 0,
            "battle_card_uniqids_2nd2": 0,
            "battle_card_uniqids_2nd3": 0,
            "battle_card_uniqids_2nd4": 0,
            "battle_card_uniqids_2nd5": 0,
            "battle_card_uniqids_2nd6": 0,
            "assist_card_uniqids_2nd1": 0,
            "assist_card_uniqids_2nd2": 0,
            "assist_card_uniqids_2nd3": 0,
            "assist_card_uniqids_2nd4": 0,
            "assist_card_uniqids_2nd5": 0,
            "assist_card_uniqids_2nd6": 0,
            "battle_card_uniqids_3rd1": 0,
            "battle_card_uniqids_3rd2": 0,
            "battle_card_uniqids_3rd3": 0,
            "battle_card_uniqids_3rd4": 0,
            "battle_card_uniqids_3rd5": 0,
            "battle_card_uniqids_3rd6": 0,
            "assist_card_uniqids_3rd1": 0,
            "assist_card_uniqids_3rd2": 0,
            "assist_card_uniqids_3rd3": 0,
            "assist_card_uniqids_3rd4": 0,
            "assist_card_uniqids_3rd5": 0,
            "assist_card_uniqids_3rd6": 0,
            "select_deck_idx": [0],
            "keeps": [{}, {}, {}],
        },
        {
            "deck_trinity_type": 3,
            "deckid": 1,
            "name": "マイチーム1",
            "battle_card_uniqids_1st1": 0,
            "battle_card_uniqids_1st2": 0,
            "battle_card_uniqids_1st3": 0,
            "battle_card_uniqids_1st4": 0,
            "battle_card_uniqids_1st5": 0,
            "battle_card_uniqids_1st6": 0,
            "assist_card_uniqids_1st1": 0,
            "assist_card_uniqids_1st2": 0,
            "assist_card_uniqids_1st3": 0,
            "assist_card_uniqids_1st4": 0,
            "assist_card_uniqids_1st5": 0,
            "assist_card_uniqids_1st6": 0,
            "battle_card_uniqids_2nd1": 0,
            "battle_card_uniqids_2nd2": 0,
            "battle_card_uniqids_2nd3": 0,
            "battle_card_uniqids_2nd4": 0,
            "battle_card_uniqids_2nd5": 0,
            "battle_card_uniqids_2nd6": 0,
            "assist_card_uniqids_2nd1": 0,
            "assist_card_uniqids_2nd2": 0,
            "assist_card_uniqids_2nd3": 0,
            "assist_card_uniqids_2nd4": 0,
            "assist_card_uniqids_2nd5": 0,
            "assist_card_uniqids_2nd6": 0,
            "battle_card_uniqids_3rd1": 0,
            "battle_card_uniqids_3rd2": 0,
            "battle_card_uniqids_3rd3": 0,
            "battle_card_uniqids_3rd4": 0,
            "battle_card_uniqids_3rd5": 0,
            "battle_card_uniqids_3rd6": 0,
            "assist_card_uniqids_3rd1": 0,
            "assist_card_uniqids_3rd2": 0,
            "assist_card_uniqids_3rd3": 0,
            "assist_card_uniqids_3rd4": 0,
            "assist_card_uniqids_3rd5": 0,
            "assist_card_uniqids_3rd6": 0,
            "select_deck_idx": [0],
            "keeps": [{}, {}, {}],
        },
        {
            "deck_trinity_type": 5,
            "deckid": 1,
            "name": "マイチーム1",
            "battle_card_uniqids_1st1": 0,
            "battle_card_uniqids_1st2": 0,
            "battle_card_uniqids_1st3": 0,
            "battle_card_uniqids_1st4": 0,
            "battle_card_uniqids_1st5": 0,
            "battle_card_uniqids_1st6": 0,
            "assist_card_uniqids_1st1": 0,
            "assist_card_uniqids_1st2": 0,
            "assist_card_uniqids_1st3": 0,
            "assist_card_uniqids_1st4": 0,
            "assist_card_uniqids_1st5": 0,
            "assist_card_uniqids_1st6": 0,
            "battle_card_uniqids_2nd1": 0,
            "battle_card_uniqids_2nd2": 0,
            "battle_card_uniqids_2nd3": 0,
            "battle_card_uniqids_2nd4": 0,
            "battle_card_uniqids_2nd5": 0,
            "battle_card_uniqids_2nd6": 0,
            "assist_card_uniqids_2nd1": 0,
            "assist_card_uniqids_2nd2": 0,
            "assist_card_uniqids_2nd3": 0,
            "assist_card_uniqids_2nd4": 0,
            "assist_card_uniqids_2nd5": 0,
            "assist_card_uniqids_2nd6": 0,
            "battle_card_uniqids_3rd1": 0,
            "battle_card_uniqids_3rd2": 0,
            "battle_card_uniqids_3rd3": 0,
            "battle_card_uniqids_3rd4": 0,
            "battle_card_uniqids_3rd5": 0,
            "battle_card_uniqids_3rd6": 0,
            "assist_card_uniqids_3rd1": 0,
            "assist_card_uniqids_3rd2": 0,
            "assist_card_uniqids_3rd3": 0,
            "assist_card_uniqids_3rd4": 0,
            "assist_card_uniqids_3rd5": 0,
            "assist_card_uniqids_3rd6": 0,
            "select_deck_idx": [0],
            "keeps": [{}, {}, {}],
        },
        {
            "deck_trinity_type": 6,
            "deckid": 1,
            "name": "マイチーム1",
            "battle_card_uniqids_1st1": 0,
            "battle_card_uniqids_1st2": 0,
            "battle_card_uniqids_1st3": 0,
            "battle_card_uniqids_1st4": 0,
            "battle_card_uniqids_1st5": 0,
            "battle_card_uniqids_1st6": 0,
            "assist_card_uniqids_1st1": 0,
            "assist_card_uniqids_1st2": 0,
            "assist_card_uniqids_1st3": 0,
            "assist_card_uniqids_1st4": 0,
            "assist_card_uniqids_1st5": 0,
            "assist_card_uniqids_1st6": 0,
            "battle_card_uniqids_2nd1": 0,
            "battle_card_uniqids_2nd2": 0,
            "battle_card_uniqids_2nd3": 0,
            "battle_card_uniqids_2nd4": 0,
            "battle_card_uniqids_2nd5": 0,
            "battle_card_uniqids_2nd6": 0,
            "assist_card_uniqids_2nd1": 0,
            "assist_card_uniqids_2nd2": 0,
            "assist_card_uniqids_2nd3": 0,
            "assist_card_uniqids_2nd4": 0,
            "assist_card_uniqids_2nd5": 0,
            "assist_card_uniqids_2nd6": 0,
            "battle_card_uniqids_3rd1": 0,
            "battle_card_uniqids_3rd2": 0,
            "battle_card_uniqids_3rd3": 0,
            "battle_card_uniqids_3rd4": 0,
            "battle_card_uniqids_3rd5": 0,
            "battle_card_uniqids_3rd6": 0,
            "assist_card_uniqids_3rd1": 0,
            "assist_card_uniqids_3rd2": 0,
            "assist_card_uniqids_3rd3": 0,
            "assist_card_uniqids_3rd4": 0,
            "assist_card_uniqids_3rd5": 0,
            "assist_card_uniqids_3rd6": 0,
            "select_deck_idx": [0],
            "keeps": [{}, {}, {}],
        },
    ]


def generateDeckData(userId: int, battleCardInitUniqueId: int) -> bool:
    decks = [
        (1, 1),
        (1, 2),
        (1, 3),
        (1, 4),
        (1, 5),
        (4, 1),
        (4, 2),
        (4, 3),
        (4, 4),
        (4, 5),
        (5, 1),
        (5, 2),
        (5, 3),
        (5, 4),
        (5, 5),
    ]

    for deckInfo in decks:
        new = {
            "user_id_owner": userId,
            "deck_type": deckInfo[0],
            "deckid": deckInfo[1],
            "name": f"マイチーム{deckInfo[1]}",
            "battle_card_uniqid1": 0 if deckInfo == (1, 1) else battleCardInitUniqueId,
            "battle_card_uniqid2": 0,
            "battle_card_uniqid3": 0,
            "battle_card_uniqid4": 0,
            "battle_card_uniqid5": 0,
            "battle_card_uniqid6": 0,
            "assist_card_uniqid1": 0,
            "assist_card_uniqid2": 0,
            "assist_card_uniqid3": 0,
            "assist_card_uniqid4": 0,
            "assist_card_uniqid5": 0,
            "assist_card_uniqid6": 0,
        }

        mongo.db[COLLECTION_NAME_DECKS].insert_one(new)

    return True
