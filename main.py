
from models.gamestate import GameState
from models.player import Player
from models.team import Team
from models.play import CreatePlay

# dodgers at mets july 19 2007
players1 = [Player("Rafael Furcal"), Player("Juan Pierre"), Player("Russell Martin"), Player("Jeff Kent"), Player(
    "Luis Gonzalez"), Player("Nomar Garciaparra"), Player("James Loney"), Player("Matt Kemp"), Player("Derek Lowe")]
players2 = [Player("José Reyes"), Player("Marlon Anderson"), Player("Carlos Beltrán"), Player("David Wright"), Player(
    "Carlos Delgado"), Player("Ramón Castro"), Player("Shawn Green"), Player("Rúben Gotay"), Player("Tom Glavine")]
state = GameState(Team("Dodgers", players1), Team(
    "Giants", players2))
state.setbattingorder(1, players1)
state.setbattingorder(2, players2)
state.pitch(CreatePlay("strike"))
state.pitch(CreatePlay("single", [1, 2, 3]))
state.pitch(CreatePlay("single", [1, 2, 3]))
state.pitch(CreatePlay("single", [1, 2, 3]))
state.pitch(CreatePlay("single", [1, 2, 3]))
state.pitch(CreatePlay("single", [1, 2, 3]))
state.pitch(CreatePlay("single", [1, 2, 3]))
state.pitch(CreatePlay("single", [1, 2, 3]))
state.pitch(CreatePlay("single", [1, 2, 3]))
state.pitch(CreatePlay("single", [1, 2, 3]))
state.pitch(CreatePlay("single", [1, 2, 3]))
state.pitch(CreatePlay("single", [1, 2, 3]))
state.pitch(CreatePlay("single", [1, 2, 3]))
state.pitch(CreatePlay("single", [1, 2, 3]))
