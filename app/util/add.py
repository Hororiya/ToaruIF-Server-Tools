import time
from ..mongo import mongo, get_next_sequence_value

COLLECTION_NAME_BATTLE_CARDS = "BattleCards"
COLLECTION_NAME_ASSIST_CARDS = "AssistCards"
COLLECTION_NAME_ITEMS = "Items"
COLLECTION_NAME_COSTUMES = "Costumes"
COLLECTION_NAME_USER = "User"
COLLECTION_NAME_USER_LOGIN_DATA = "UserLoginData"
COLLECTION_NAME_USER_TITLES = "UserTitles"
COLLECTION_NAME_USER_STATUS = "UserStatus"
COLLECTION_NAME_DECKS = "Decks"
COLLECTION_NAME_MONEY = "Money"
COLLECTION_NAME_MENU_DECORATION_INFOS = "MenuDecorations"


def addBattleCard(userId: int, battleCardKey: int) -> bool:
    new = {
        "user_owner_id": userId,
        "battle_card_uniqid": 0,
        "battle_cardid": battleCardKey,
        "card_grow_rank": 1,
        "card_grow_exp": 0,
        "card_grow_limit_break_count": 1,
        "card_grow_status_rank": 1,
        "card_grow_statusup_node_flag": 0,
        "card_grow_skill_rank1": 1,
        "card_grow_skill_rank2": 1,
        "card_grow_skill_rank3": 1,
        "card_grow_skill_rank4": 1,
        "card_grow_skill_rank5": 1,
        "card_grow_potential_skill_rank1": 1,
        "card_grow_potential_skill_rank2": 1,
        "card_grow_potential_skill_rank3": 1,
        "card_grow_awaken_status_str_int_idx": 0,
        "card_grow_awaken_status_vit_idx": 0,
        "card_grow_awaken_status_mind_idx": 0,
        "card_grow_awaken_status_hp_idx": 0,
        "card_limit_break_buy_total": 0,
    }

    check = mongo.db[COLLECTION_NAME_BATTLE_CARDS].find_one(
        {"user_owner_id": userId, "battle_cardid": battleCardKey}
    )
    if not check:
        # New card
        new["battle_card_uniqid"] = get_next_sequence_value(
            COLLECTION_NAME_BATTLE_CARDS
        )
        mongo.db[COLLECTION_NAME_BATTLE_CARDS].insert_one(new)
    else:
        # Exists, rankup items
        new = check
        # TODO
        mongo.db[COLLECTION_NAME_BATTLE_CARDS].replace_one(
            {"user_owner_id": userId, "battle_cardid": battleCardKey}, new
        )

    return new


def addAssistCard(userId: int, assistCardKey: int) -> bool:
    new = {
        "user_owner_id": userId,
        "assist_card_uniqid": 0,
        "assist_cardid": assistCardKey,
        "is_lock": 0,
        "card_grow_rank": 1,
        "card_grow_exp": 0,
        "card_grow_limit_break_count": 1,
        "card_grow_status_rank": 1,
        "card_grow_statusup_node_flag": 0,
        "card_grow_skill_rank1": 1,
        "card_grow_skill_rank2": 1,
        "card_grow_skill_rank3": 1,
        "card_grow_skill_rank4": 1,
        "card_grow_skill_rank5": 1,
        "card_grow_potential_skill_rank1": 1,
        "card_grow_potential_skill_rank2": 1,
        "card_grow_potential_skill_rank3": 1,
        "card_grow_awaken_status_str_int_idx": 0,
        "card_grow_awaken_status_vit_idx": 0,
        "card_grow_awaken_status_mind_idx": 0,
        "card_grow_awaken_status_hp_idx": 0,
        "card_limit_break_buy_total": 0,
    }

    check = mongo.db[COLLECTION_NAME_ASSIST_CARDS].find_one(
        {"user_owner_id": userId, "assist_card_uniqid": assistCardKey}
    )
    if not check:
        # New card
        new["assist_card_uniqid"] = get_next_sequence_value(
            COLLECTION_NAME_ASSIST_CARDS
        )
        mongo.db[COLLECTION_NAME_ASSIST_CARDS].insert_one(new)
    else:
        # Exists, rankup items
        new = check
        # TODO
        mongo.db[COLLECTION_NAME_ASSIST_CARDS].replace_one(
            {"user_owner_id": userId, "assist_card_uniqid": assistCardKey}, new
        )

    return new


def addItem(userId: int, itemId: int, amount: int) -> bool:
    new = {
        "user_owner_id": userId,
        "uniqid": 359162436001,
        "itemid": itemId,
        "param": 0,
        "num": amount,
        "total": amount,
    }

    return new


def addCostume(userId: int, costumeId: int) -> bool:
    new = {"user_owner_id": userId, "costumeid": costumeId, "flag": 2}


def addUser(userId: int) -> object:
    new = {
        "userid": userId,
        "name": "",
        "comment": "",
        "profile_cardid": 200212001,
        "last_system_presentid": 0,
        "paypoint_appstore": 0,
        "paypoint_appstore_free": 0,
        "paypoint_googleplay": 0,
        "paypoint_googleplay_free": 0,
        "paypoint_free": 0,
        "paypoint_is_err_bridge": 0,
        "paypoint_bridge_ref": 0,
        "paypoint_bridge_free_ref": 0,
    }

    mongo.db[COLLECTION_NAME_USER].insert_one(new)

    return new


def addUserLoginData(uuid: str) -> object:
    new = {
        "uuid": uuid,
        "userId": get_next_sequence_value(COLLECTION_NAME_USER),
        "inviteId": 200000000 + get_next_sequence_value("Invites"),
        "tutorialStatus": 0,  # 0 is Todo, 1 is Done
        "tutorialType": 1,
        "tutorialIndex": 1,
        "tutorialClearDate": "1970-01-01 09:00:00",
    }

    mongo.db[COLLECTION_NAME_USER_LOGIN_DATA].insert_one(new)

    return new


def addUserTitle(userId: int, userTitleId: int) -> object:
    new = {
        "user_owner_id": userId,
        "user_titleid": userTitleId,
        "user_title_param": 0,
        "state": 1,
        "received_time": int(time.time()),
    }

    mongo.db[COLLECTION_NAME_USER_TITLES].insert_one(new)

    return new


def addUserMoney(userId: int, type: int, num: int, param: int = 0) -> object:
    new = {"user_owner_id": userId, "type": type, "param": param, "num": num}

    mongo.db[COLLECTION_NAME_MONEY].insert_one(new)
    check = mongo.db[COLLECTION_NAME_MONEY].find_one(
        {"user_owner_id": userId, "type": type, "param": param}
    )
    if not check:
        # New card
        new["num"] += num
        mongo.db[COLLECTION_NAME_MONEY].insert_one(new)
    else:
        # Exists, add money
        new = check
        # TODO
        mongo.db[COLLECTION_NAME_MONEY].replace_one(
            {"user_owner_id": userId, "type": type, "param": param}, new
        )
    return new

# onInit only
def addUserStatus(userId: int):
    new = {
        "user_owner_id": userId,
        "rank": 1,
        "total_exp": 0,
        "favorite_charaid1": 1,
        "favorite_cardid1": 100111001,
        "favorite_card_effect_on1": 0,
        "favorite_costumeid1": 0,
        "favorite_costume_anime_on1": 0,
        "favorite_charaid2": 0,
        "favorite_cardid2": 0,
        "favorite_card_effect_on2": 0,
        "favorite_costumeid2": 0,
        "favorite_costume_anime_on2": 0,
        "favorite_charaid3": 0,
        "favorite_cardid3": 0,
        "favorite_card_effect_on3": 0,
        "favorite_costumeid3": 0,
        "favorite_costume_anime_on3": 0,
        "favorite_charaid4": 0,
        "favorite_cardid4": 0,
        "favorite_card_effect_on4": 0,
        "favorite_costumeid4": 0,
        "favorite_costume_anime_on4": 0,
        "favorite_charaid5": 0,
        "favorite_cardid5": 0,
        "favorite_card_effect_on5": 0,
        "favorite_costumeid5": 0,
        "favorite_costume_anime_on5": 0,
        "favorite_charaid6": 0,
        "favorite_cardid6": 0,
        "favorite_card_effect_on6": 0,
        "favorite_costumeid6": 0,
        "favorite_costume_anime_on6": 0,
        "meet_favorite_chara_idx": 0,
        "chara_meet_time": 0,
        "quest_complete_num": 0,
        "battle_card_num": 2,
        "assist_card_num": 1,
        "quest_badge_state": 0,
        "select_user_titleid": 70031001,
        "select_user_title_param": 0,
        "total_chara_power": 0,
    }
    
    mongo.db[COLLECTION_NAME_USER_STATUS].insert_one(new)
    
    return new

def setDecorations(userId: int, decorations: list):
    obj = {
        "user_owner_id": userId,
        "decorations": decorations
    }
    
    check = mongo.db[COLLECTION_NAME_MENU_DECORATION_INFOS].find_one({"user_owner_id": userId})
    
    if check:
        mongo.db[COLLECTION_NAME_MENU_DECORATION_INFOS].replace_one({"user_owner_id": userId}, obj)
    else:
        mongo.db[COLLECTION_NAME_MENU_DECORATION_INFOS].insert_one(obj)