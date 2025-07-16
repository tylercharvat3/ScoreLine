from models.team import Team
from models.player import Player
from typing import List


class GameState:
    def __init__(self, team1: Team, team2: Team):
        self.team1 = team1  # away team
        self.team2 = team2  # home team
        self.inning = 1
        self.isTop = True
        self.bases = [None, None, None]
        self.score = [0, 0]  # [away, home]
        self.count = [0, 0]  # [balls, strikes]
        self.activeBatter = ""
        self.outs = 0

    def showState(self):
        print(
            f"{self.team1.name}: {self.score[0]}, {self.team2.name}: {self.score[1]}")
        print(
            f"{self.count[0]} ball{"s" if self.count[0] != 1 else ""}, {self.count[1]} strike{"s" if self.count[1] != 1 else ""}")
        print((f"{self.outs} outs"))
        print(f"Runners: {self.bases[0]} {self.bases[1]} {self.bases[2]}")

    def setbattingorder(self, team: int, order: List[Player]):
        if team == 1:
            self.team1.setBattingOrder(order)
        if team == 2:
            self.team2.setBattingOrder(order)

    def pitch(self, result):
        # result can be strike, ball, in play(single, double, triple, hr, hbp, walk, error, flyout, strikeout, strikeout_looking, lineout, putout(number-number))
        match result:
            case "strike":
                self.count[1] += 1
            case "ball":
                self.count[0] += 1
            case _:
                self.inPlay(result)

    def inPlay(self, result):
        match result:
            case "single":
                self.bases[0] = self.activeBatter
            case "double":
                self.bases[1] = self.activeBatter
            case "triple":
                self.bases[2] = self.activeBatter
