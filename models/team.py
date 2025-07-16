from models.player import Player
from typing import List


class Team:
    def __init__(self, name, roster: List[Player]):
        self.name = name
        self.roster = roster
        self.battingOrder = []

    def setBattingOrder(self, order: List[Player]):
        self.battingOrder = order
