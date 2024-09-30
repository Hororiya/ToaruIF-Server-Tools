import json
from flask import Blueprint
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
    success = [
        {
            "res_code": 0,
            "res_str": "OK",
            "server_time": 1727283075,
            "session_time": 1727284874,
            "patch_version": 145474,
            "tag_schedule_version": 14200,
        },
        {
            "hand_shake": {"userid": 1587615},
            "do_create_user": 0,
            "tutorial_download_idx": 1,
            "inviteid": 260026556,
        },
    ]

    return prepareResponse(success, 200)


# TODO proper implementation
@main_blueprint.route("/api/GetOnceDiffResultAll2", methods=["POST"])
def GetOnceDiffResultAll2():
    data = [{}, {}, {}]
    data = json.load(open("./sample/sampleResponseDiff.json", "r"))
    data[0] = getMainResponseData(0)
    data[1] = {}
    # Diff
    data[2]["server_const"] = Config.GAME_CONSTS
    data[2]["user_device"][0]["modify"] = getArenaData(0)
    data[2]["user_play_dungeon"][0]["modify"] = getPlayDungeonData(0)
    data[2]["user_story"][0]["modify"] = getUserStoryInfo(0)
    data[2]["user_deck_trinity_type"][0]["modify"] = getDeckTrinityType(0)
    data[2]["user_dungeon"][0]["modify"] = getDungeonData(0)
    data[2]["user_guild_battle"][0]["modify"] = getGuildBattleData(0)
    data[2]["user_battle"][0]["modify"] = getBattlePlayState(0)
    data[2]["user_limited_point"][0]["modify"] = []
    data[2]["user_chara"][0]["modify"] = getCharaData(0)
    data[2]["user_status"][0]["modify"] = getUserStatusData(0)
    data[2]["user_battle_bstg"][0]["modify"] = getBattleBstgData(0)
    data[2]["user_stamp"][0]["modify"] = getUserStamps(0)
    data[2]["user_play_quest"][0]["modify"] = [{"questid": 0, "state": 0}]
    data[2]["user_tutorial"][0]["modify"] = getUserTutorial(0)
    data[2]["user_money"][0]["modify"] = getUserMoney(0)
    data[2]["user_guild"][0]["modify"] = getGuildData(0)
    data[2]["event_top_cache"][0]["modify"] = getEventTopCacheData(0)
    data[2]["user_mission"][0]["modify"] = []
    data[2]["user_play_raid"][0]["modify"] = getRaidData(0)
    data[2]["user_deck_type"][0]["modify"] = getDeckType(0)
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
    data[2]["user_trial_quest"][0]["modify"] = getTrialCommonData(0)
    data[2]["user_item"][0]["modify"] = getTrialCommonData(0)
    data[2]["user_flag"][0]["modify"] = getTrialCommonData(0)
    data[2]["user_present_box_count_cache"][0]["modify"] = [{"count": 0}]
    data[2]["user"][0]["modify"] = getUserData(0)
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
    data[2]["user_limit_story"][0]["modify"] = getUserLimitStory(0)
    data[2]["user_costume"][0]["modify"] = getUserCostume(0)
    data[2]["user_shop"][0]["modify"] = getShop()
    data[2]["user_deck"][0]["modify"] = getDeckInfo(0)
    data[2]["user_deck_trinity"][0]["modify"] = getDeckTrinityInfo(0)
    data[2]["user_legion"][0]["modify"] = getLegionData(0)
    data[2]["user_play_story"][0]["modify"] = getUserPlayStoryInfo(0)
    data[2]["user_guild_stamina_trade"][0]["modify"] = getGuildStaminaTradeData(0)
    data[2]["user_shop_lineup"][0]["modify"] = getShopLineupData()
    data[2]["trial_common"][0]["modify"] = getTrialCommonData(0)
    data[2]["user_user_title"][0]["modify"] = getUserTitle(0)
    data[2]["user_battle_card"][0]["modify"] = getBattleCardsData(0)
    data[2]["user_battle_card"][0]["modify"] = getBattleCardsData(0)
    data[2]["user_assist_card"][0]["modify"] = getAssistCardsData(0)
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
    data = json.load(open("./sample/sampleResponseHome2.json", "r"))
    return prepareResponse(data, 200)


@main_blueprint.route("/api/GetHome2_2", methods=["POST"])
def GetHome2_2():
    data = json.load(open("./sample/sampleResponseHome2_2.json", "r"))
    return prepareResponse(data, 200)


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
