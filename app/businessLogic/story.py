# Flags:
# 0 = not done?
# 15 = done 100%?
# 5 = half done?

# State:
# 5 = cleared?
# 2 = ???
# 1 = todo?

# Sample Reward
# {"type": 11, "id": 0, "num": 20, "param1": 0, "param2": 0, "param3": 0, "rarity": 0}


def getUserStoryInfo(userId: int) -> list:
    # TODO logic
    return []


def getUserPlayStoryInfo(userId: int) -> list:
    return [{"storyid": 0, "state": 0, "limit_story_uniqid": 0}]

def getUserLimitStory(userId: int) -> list:
    return []