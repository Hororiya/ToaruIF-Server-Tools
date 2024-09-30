import json

ASSIST_CARD_DATA = json.load(open("./data/AssistCard.json", "r"))["items"]
BATTLE_CARD_DATA = json.load(open("./data/BattleCard.json", "r"))["items"]


def getAssistCardsData(userId: int) -> list:
    out = []
    id = 1
    for assist in ASSIST_CARD_DATA:
        out.append(
            {
                "assist_card_uniqid": id,
                "assist_cardid": assist["key"],
                "is_lock": 0,
                "card_grow_rank": 1,
                "card_grow_exp": 0,
                "card_grow_limit_break_count": 6,
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
        )
        id += 1

    return out


def getBattleCardsData(userId: int) -> list:
    out = []
    id = 1092285001
    for battle in BATTLE_CARD_DATA:
        out.append(
            {
                "battle_card_uniqid": id,
                "battle_cardid": battle['key'],
                "card_grow_rank": 1,
                "card_grow_exp": 0,
                "card_grow_limit_break_count": 6,
                "card_grow_status_rank": 1,
                "card_grow_statusup_node_flag": 3,
                "card_grow_skill_rank1": 3,
                "card_grow_skill_rank2": 3,
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
        )
        id += 1
        
    return out
