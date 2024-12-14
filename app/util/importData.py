import json

ASSIST_CARD_DATA = json.load(open("./data/AssistCard.json", "r"))["items"]
BATTLE_CARD_DATA = json.load(open("./data/BattleCard.json", "r"))["items"]
STORY_DATA = json.load(open("./data/Story.json", "r"))
