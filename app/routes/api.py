import json
import time
from flask import Blueprint, request
from ..mongo import mongo
from ..util.authData import getAuthData
from ..util.add import COLLECTION_NAME_USER_LOGIN_DATA, addUserLoginData, addUser
from ..util.prepareResponse import prepareResponse
from ..businessLogic.card import getBattleCardsData, getAssistCardsData
from ..businessLogic.user import (
    getUserCostume,
    getUserMoney,
    getUserStamps,
    getUserStatusData,
    getUserTitle,
    getUserTutorial,
    getUserData,
    createUser,
    changeName,
    saveUserTutorialStatus,
    clearUserTutorialStatus,
)
from ..businessLogic.arena import getArenaData
from ..businessLogic.dungeon import getDungeonData, getPlayDungeonData
from ..businessLogic.story import (
    getUserStoryInfo,
    getUserLimitStory,
    getUserPlayStoryInfo,
)
from ..businessLogic.deck import (
    getDeckInfo,
    getDeckTrinityInfo,
    getDeckTrinityType,
    getDeckType,
)
from ..businessLogic.guild import (
    getGuildBattleData,
    getGuildData,
    getGuildStaminaTradeData,
)
from ..businessLogic.battle import getBattleBstgData, getBattlePlayState
from ..businessLogic.chara import getCharaData
from ..businessLogic.event import getEventTopCacheData
from ..businessLogic.raid import getRaidData
from ..businessLogic.trial import getTrialCommonData
from ..businessLogic.shop import getShopLineupData, getShop
from ..businessLogic.legion import getLegionData
from ..util.mainResponseData import getMainResponseData
from ..config import Config

main_blueprint = Blueprint("api", __name__)


# socialsv components
@main_blueprint.route("/api/Connect", methods=["POST"])
def Connect():

    token = request.cookies.get("sk")
    if not token:
        return prepareResponse({}, 401)

    data = getAuthData(sessionKey=token)

    created = False
    loggedInData = mongo.db[COLLECTION_NAME_USER_LOGIN_DATA].find_one(
        {"userId": data["userId"]}
    )

    if not loggedInData:
        created = True
        loggedInData = addUserLoginData(data["uuid"])

    success = [
        {
            "res_code": 0,
            "res_str": "OK",
            "server_time": int(time.time()),
            "session_time": int(time.time()),
            "patch_version": Config.RES_VER,
            "tag_schedule_version": Config.TAG_SCHEDULE,
        },
        {
            "hand_shake": {"userid": loggedInData["userId"]},
            "do_create_user": 1 if created else 0,
            "tutorial_download_idx": 1,
            "inviteid": loggedInData["inviteId"],
        },
    ]

    return prepareResponse(success, 200)


# TODO proper implementation
@main_blueprint.route("/api/GetOnceDiffResultAll2", methods=["POST"])
def GetOnceDiffResultAll2():
    token = request.cookies.get("sk")
    if not token:
        return prepareResponse({}, 401)

    data = getAuthData(sessionKey=token)
    userId = data["userId"]

    data = [{}, {}, {}]
    data = json.load(open("./sample/sampleResponseDiff.json", "r"))
    data[0] = getMainResponseData(userId)
    data[1] = {}
    # Diff
    data[2]["server_const"] = Config.GAME_CONSTS
    data[2]["user_device"][0]["modify"] = getArenaData(userId)
    data[2]["user_play_dungeon"][0]["modify"] = getPlayDungeonData(userId)
    data[2]["user_story"][0]["modify"] = getUserStoryInfo(userId)
    data[2]["user_deck_trinity_type"][0]["modify"] = getDeckTrinityType(userId)
    data[2]["user_dungeon"][0]["modify"] = getDungeonData(userId)
    data[2]["user_guild_battle"][0]["modify"] = getGuildBattleData(userId)
    data[2]["user_battle"][0]["modify"] = getBattlePlayState(userId)
    data[2]["user_limited_point"][0]["modify"] = []
    data[2]["user_chara"][0]["modify"] = getCharaData(userId)
    data[2]["user_status"][0]["modify"] = getUserStatusData(userId)
    data[2]["user_battle_bstg"][0]["modify"] = getBattleBstgData(userId)
    data[2]["user_stamp"][0]["modify"] = getUserStamps(userId)
    data[2]["user_play_quest"][0]["modify"] = [{"questid": 0, "state": 0}]
    data[2]["user_tutorial"][0]["modify"] = getUserTutorial(userId)
    data[2]["user_money"][0]["modify"] = getUserMoney(userId)
    data[2]["user_guild"][0]["modify"] = getGuildData(userId)
    data[2]["event_top_cache"][0]["modify"] = getEventTopCacheData(userId)
    data[2]["user_mission"][0]["modify"] = []
    data[2]["user_play_raid"][0]["modify"] = getRaidData(userId)
    data[2]["user_deck_type"][0]["modify"] = getDeckType(userId)
    data[2]["user_spot"][0]["modify"] = [
        {
            "spotid": 1,
            "spawn_spot_eventid": 0,
            "spawn_event_state": 0,
            "spawn_before_rarity": 0,
            "spawn_event_type": 0,
            "spawn_is_first_clear": 0,
            "spawn_after_rarity": 0,
            "spawn_limit_story_uniqid": 0,
        }
    ]
    data[2]["user_trial_quest"][0]["modify"] = getTrialCommonData(userId)
    data[2]["user_item"][0]["modify"] = getTrialCommonData(userId)
    data[2]["user_flag"][0]["modify"] = getTrialCommonData(userId)
    data[2]["user_present_box_count_cache"][0]["modify"] = [{"count": 0}]
    data[2]["user"][0]["modify"] = getUserData(userId)
    data[2]["user_trial_stage"][0]["modify"] = [{"stageid": 1, "state": 2}]
    data[2]["user_play_guild_battle"][0]["modify"] = [
        {
            "guild_battleid": 0,
            "state": 0,
            "show_enemy_level": 0,
            "battle_stage_id": 0,
            "bgm": 0,
        }
    ]
    data[2]["user_event"][0]["modify"] = [
        {
            "eventid": 401,
            "received_total": 0,
            "keep_boss_hp_normal": -1,
            "keep_boss_hp_hard": -1,
            "keep_boss_hp_very_hard": -1,
            "keep_boss_hp_very_hard_no_limit": -1,
        }
    ]
    data[2]["user_limit_story"][0]["modify"] = getUserLimitStory(userId)
    data[2]["user_costume"][0]["modify"] = getUserCostume(userId)
    data[2]["user_shop"][0]["modify"] = getShop()
    data[2]["user_deck"][0]["modify"] = getDeckInfo(userId)
    data[2]["user_deck_trinity"][0]["modify"] = getDeckTrinityInfo(userId)
    data[2]["user_legion"][0]["modify"] = getLegionData(userId)
    data[2]["user_play_story"][0]["modify"] = getUserPlayStoryInfo(userId)
    data[2]["user_guild_stamina_trade"][0]["modify"] = getGuildStaminaTradeData(userId)
    data[2]["user_shop_lineup"][0]["modify"] = getShopLineupData()
    data[2]["trial_common"][0]["modify"] = getTrialCommonData(userId)
    data[2]["user_user_title"][0]["modify"] = getUserTitle(userId)
    data[2]["user_battle_card"][0]["modify"] = getBattleCardsData(userId)
    data[2]["user_assist_card"][0]["modify"] = getAssistCardsData(userId)
    return prepareResponse(data, 200)


# TODO proper implementation
@main_blueprint.route("/api/GetUser", methods=["POST"])
def GetUser():
    data = json.load(open("./sample/sampleResponseUser.json", "r"))
    return prepareResponse(data, 200)


# TODO proper implementation
@main_blueprint.route("/api/PurchaseCheck", methods=["POST"])
def PurchaseCheck():
    data = json.load(open("./sample/sampleResponsePurchaseCheck.json", "r"))
    return prepareResponse(data, 200)


@main_blueprint.route("/api/GetHome2", methods=["POST"])
def GetHome2():
    # data = json.load(open("./sample/sampleResponseHome2.json", "r"))

    _res = {
        "login_bonuses": [],
        "banners": [],
        "login_bonus_before_notices": [],
        "arena_class_info": [{"best_class": 23, "last_class": 23}],
        "is_entry_arena_class": [0],
        "is_invite_user": 0,
        "is_invited_user": 1,
    }

    return prepareResponse(
        [getMainResponseData(0), _res, {}],
        200,
    )


@main_blueprint.route("/api/GetHome2_2", methods=["POST"])
def GetHome2_2():
    # data = json.load(open("./sample/sampleResponseHome2_2.json", "r"))

    _res = {
        "login_bonuses": [],
        "banners": [
            {
                "image_url": "http://cache.index-if.jp/web/GcxbUMTtDG8kq8H2VvfV5hPJs.ifpng",
                "complete_count": [
                    {
                        "type": 31,
                        "param_1st": 600,
                        "param_2nd": 0,
                        "param_3rd": 0,
                        "record_count_type": 0,
                        "flag_type": 0,
                        "flag_type_param": 0,
                        "mission_user_flag_type": 0,
                    }
                ],
                "schedule": {
                    "start_time": 1727208000,
                    "end_time": 1728849599,
                    "open_time": 1727208000,
                    "close_time": 1728849599,
                },
            }
        ],
        "login_bonus_before_notices": [],
        "arena_class_info": [{"best_class": 23, "last_class": 23}],
        "is_entry_arena_class": [0],
        "is_invite_user": 0,
        "is_invited_user": 1,
    }
    return prepareResponse([getMainResponseData(0), _res, {}], 200)


@main_blueprint.route("/api/StartStory", methods=["POST"])
def StartStory():
    # ID: 927040001
    data = json.load(open("./sample/sampleResponseStartStory.json", "r"))
    return prepareResponse(data, 200)


@main_blueprint.route("/web/")
def WebRoot():
    return "HTML missing lmao."


@main_blueprint.route("/api/GetGachaList", methods=["POST"])
def GachaList():
    # ID: 927040001
    data = json.load(open("./sample/sampleResponseGachaList.json", "r"))
    return prepareResponse(data, 200)


# CompleteSubTutorial
# {"sub_tutorial_idx":55}
@main_blueprint.route("/api/CompleteSubTutorial", methods=["POST"])
def CompleteSubTutorial():
    # ID: 927040001
    # data = json.load(open("./sample/sampleResponseGachaList.json", "r"))
    return prepareResponse([getMainResponseData(0), {}], 200)


@main_blueprint.route("/api/CreateUser", methods=["POST"])
def CreateUser():
    token = request.cookies.get("sk")
    if not token:
        return prepareResponse({}, 401)

    data = getAuthData(sessionKey=token)
    userId = data["userId"]

    _r = createUser(userId)

    return prepareResponse([getMainResponseData(0), {}], 200)


@main_blueprint.route("/api/ChangeUserName", methods=["POST"])
def ChangeUserName():
    token = request.cookies.get("sk")
    if not token:
        return prepareResponse({}, 401)

    data = getAuthData(sessionKey=token)
    userId = data["userId"]

    data = request.get_json(force=True)  # Get the JSON data

    usrData = changeName(userId=userId, name=data["name"])
    # Tutorial check
    tutorial = getUserTutorial(userId=userId)
    if tutorial[0]["complete_flag"] == 0:
        tutorial[0]["play_tutorial_idx"] = 2

    return prepareResponse(
        [
            getMainResponseData(userId=userId),
            {},
            {"user_tutorial": [{"modify": tutorial}], "user": [{"modify": usrData}]},
        ]
    )


@main_blueprint.route("/api/NextTutorial", methods=["POST"])
def NextTutorial():
    token = request.cookies.get("sk")
    if not token:
        return prepareResponse({}, 401)

    data = getAuthData(sessionKey=token)
    userId = data["userId"]

    status = {
        1: 3,
        2: 3,
        3: 4,
        4: 5,
        5: 6,
        6: 7,
    }

    tutorial = getUserTutorial(userId=userId)
    tutorial[0]["play_tutorial_idx"] = status[tutorial[0]["play_tutorial_idx"]]

    saveUserTutorialStatus(
        userId, tutorial[0]["play_tutorial_type"], tutorial[0]["play_tutorial_idx"]
    )

    return prepareResponse(
        [
            getMainResponseData(userId=userId),
            {},
            {"user_tutorial": [{"modify": tutorial}]},
        ]
    )


@main_blueprint.route("/api/DownloadTutorial", methods=["POST"])
def DownloadTutorial():
    token = request.cookies.get("sk")
    if not token:
        return prepareResponse({}, 401)

    data = getAuthData(sessionKey=token)
    userId = data["userId"]

    clearUserTutorialStatus(userId)
    tutorial = getUserTutorial(userId=userId)

    return prepareResponse(
        [
            getMainResponseData(userId=userId),
            {},
            {"user_tutorial": [{"modify": tutorial}]},
        ]
    )
