COLLECTION_NAME_USER_STATUS = "UserStatus"


def getUserStatusData(userId: int) -> list:
    # TODO proper logic
    return [
        {
            "rank": 999,
            "total_exp": 9999999,
            "favorite_charaid1": 30,
            "favorite_cardid1": 0,
            "favorite_card_effect_on1": 0,
            "favorite_costumeid1": 30000401,
            "favorite_costume_anime_on1": 1,
            "favorite_charaid2": 10,
            "favorite_cardid2": 201030002,
            "favorite_card_effect_on2": 0,
            "favorite_costumeid2": 0,
            "favorite_costume_anime_on2": 0,
            "favorite_charaid3": 13,
            "favorite_cardid3": 701330001,
            "favorite_card_effect_on3": 0,
            "favorite_costumeid3": 0,
            "favorite_costume_anime_on3": 0,
            "favorite_charaid4": 181,
            "favorite_cardid4": 618130001,
            "favorite_card_effect_on4": 0,
            "favorite_costumeid4": 0,
            "favorite_costume_anime_on4": 0,
            "favorite_charaid5": 69,
            "favorite_cardid5": 206933001,
            "favorite_card_effect_on5": 0,
            "favorite_costumeid5": 0,
            "favorite_costume_anime_on5": 0,
            "favorite_charaid6": 45,
            "favorite_cardid6": 0,
            "favorite_card_effect_on6": 0,
            "favorite_costumeid6": 45000901,
            "favorite_costume_anime_on6": 1,
            "meet_favorite_chara_idx": 4,
            "chara_meet_time": 0,
            "quest_complete_num": 379,
            "battle_card_num": 98,
            "assist_card_num": 96,
            "quest_badge_state": 0,
            "select_user_titleid": 30691000,
            "select_user_title_param": 0,
            "total_chara_power": 450399,
        }
    ]


def getUserStamps(userId: int) -> list:
    # TODO proper logic
    out = []
    for i in range(1, 8):
        out.append({"stampid": i})
    return out


def getUserTutorial(userId: int) -> list:
    # TODO proper logic
    return [
        {
            "complete_flag": 16126,
            "play_tutorial_type": 0,
            "play_tutorial_idx": 0,
            "prologue_finish_time": "2019-07-09 23:11:45",
        }
    ]


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
    return [
        {
            "userid": 1587615,
            "name": "Ray",
            "comment": "Twitter: @RayFirefist",
            "profile_cardid": 206933001,
            "last_system_presentid": 403,
            "paypoint_appstore": 0,
            "paypoint_appstore_free": 0,
            "paypoint_googleplay": 0,
            "paypoint_googleplay_free": 0,
            "paypoint_free": 0,
            "paypoint_is_err_bridge": 0,
            "paypoint_bridge_ref": 0,
            "paypoint_bridge_free_ref": 999999,
        }
    ]
