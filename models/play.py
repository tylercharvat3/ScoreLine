from typing import Dict, List


class Play:
    def __init__(self, result):
        self.result = result


class InPlay:
    def __init__(self, play: Play, baserunnerChanges: List[int]):
        self.result = play.result
        self.baserunnerChanges = baserunnerChanges

    def getBaseChanges(self, state):
        oldBases = state.bases
        newBases = [None, None, None, None, None, None]
        newBases[self.baserunnerChanges[0]] = oldBases[0]
        newBases[self.baserunnerChanges[1]] = oldBases[1]
        newBases[self.baserunnerChanges[2]] = oldBases[2]
        return newBases


def CreatePlay(result: str, baserunnerChanges: List[int] = None):
    play = Play(result)
    if baserunnerChanges is not None:
        print(baserunnerChanges)
        return InPlay(play, baserunnerChanges)
    return play
