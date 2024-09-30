def getGuildBattleData(userId: int) -> list:
    # TODO proper logic
    return [
        {"guild_battleid": 21005, "next_start_time": 1601236800},
        {"guild_battleid": 21017, "next_start_time": 1648324800},
        {"guild_battleid": 21500, "next_start_time": 1596139200},
    ]


def getGuildData(userId: int) -> list:
    return [
        {
            "cache_guildid": 0,
            "post_type": 0,
            "user_guild_exp_point_num": 0,
            "last_home_time": "2024-09-26 00:14:48",
            "penalty_time": 1622840246,
            "play_guild_battle_league_event_topid": 0,
        }
    ]


def getGuildStaminaTradeData(userId: int) -> list:
    return [
        {
            "difficulty": 1,
            "total_gauge": 610,
            "trade_rank": 7,
            "next_trade_time": "2022-07-22 05:00:00",
        }
    ]
