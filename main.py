
from models.gamestate import GameState
from models.player import Player
from models.team import Team


state = GameState(Team("Dodgers", [Player("Will Smith")]), Team(
    "Giants", [Player("Buster Posey")]))

state.pitch("strike")
state.pitch("strike")
state.pitch("ball")
state.pitch("single")
state.showState()
