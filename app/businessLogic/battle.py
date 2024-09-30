def getBattlePlayState(userId: int) -> list:
    # TODO pause play state
    return [{"play_state": 0}]


def getBattleBstgData(userId: int) -> list:
    # TODO proper logic
    return [{"worker_type": 4, "play_state": 0}, {"worker_type": 8, "play_state": 0}]
