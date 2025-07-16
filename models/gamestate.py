from models.team import Team
from models.player import Player
from models.play import InPlay, Play, CreatePlay
from typing import List, Union


class GameState:
    def __init__(self, team1: Team, team2: Team):
        self.team1 = team1  # away team
        self.team2 = team2  # home team
        self.inning = 1
        self.isTop = True
        self.bases = [None, None, None, None]
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
        print(
            f"Runners: "
            f"{self.bases[0].name if self.bases[0] else 'None'} "
            f"{self.bases[1].name if self.bases[1] else 'None'} "
            f"{self.bases[2].name if self.bases[2] else 'None'}"
        )

    def setBases(self, bases):
        for i in [3, 4, 5]:
            if i < len(bases) and bases[i] is not None:
                if self.isTop:
                    self.score[0] += 1
                else:
                    self.score[1] += 1
        self.bases = bases[:3]

    def nextBatter(self):
        self.count = [0, 0]
        if (self.isTop):
            self.activeBatter = self.team1.battingOrder[(self.team1.battingOrder.index(
                self.activeBatter)+1) % 9]

    def setbattingorder(self, team: int, order: List[Player]):
        if team == 1:
            self.team1.setBattingOrder(order)
            self.activeBatter = order[0]
        if team == 2:
            self.team2.setBattingOrder(order)

    def pitch(self, play: Union[Play, InPlay]):
        # result can be strike, ball, in play(single, double, triple, hr, hbp, walk, error, flyout, strikeout, strikeout_looking, lineout, putout(number-number))
        match play.result:
            case "strike":
                self.count[1] += 1
            case "ball":
                self.count[0] += 1
            case "single":
                self.setBases(play.getBaseChanges(self))
                self.bases[0] = self.activeBatter
                self.nextBatter()
        self.showState()
