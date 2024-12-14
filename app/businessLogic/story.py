from ..util.importData import STORY_DATA

# Flags:
# 0 = not done?
# 15 = done 100%?
# 5 = half done?

# State:
# 0 : None
# 1 : Close
# 2 : Open
# 3 : Played
# 4 : OnceRewardWait
# 5 : OnceRewardReceived
# 6 : OnceRewardNone
# 7 : ClearClose

# Sample Reward
# {"type": 11, "id": 0, "num": 20, "param1": 0, "param2": 0, "param3": 0, "rarity": 0}

def getUserStoryInfo(userId: int) -> list:
    # TODO logic
    out = []
    for story in STORY_DATA:
        out.append(
            [
                {
                    "storyid": story["key"],
                    "state": 5,
                    "subgoal_flag": 15
                }
            ]
        )

    return out


def getUserPlayStoryInfo(userId: int) -> list:
    return [{"storyid": 0, "state": 0, "limit_story_uniqid": 0}]


def getUserLimitStory(userId: int) -> list:
    return []
