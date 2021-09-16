# package exercises

#
#  Simulation of LCR game. See, https://www.wikihow.com/Play-LCR
#
from typing import List


# ------- Class to hold player data -----------
class Player:
    def __init__(self, name: str, chips: int):
        self.name = name
        self.chips = chips


def lcr_program():
    # test()    # < --- Uncomment to run tests ---

    # Hard coded data
    players: List[Player] = [Player("olle", 3),
                             Player("fia", 3),
                             Player("pelle", 3)]
    current: Player = players[0]
    print("Simulation starts")
    display_players(players)

    # TODO Run the simulation

    # ---- Logical methods -----------------

    # TODO


# --- IO methods ------------------
def display_state(actual: Player, result: str, players: List[Player]):
    print(actual.name + " got ", end='')
    print(result)
    display_players(players)


def display_players(players: List[Player]):
    for player in players:
        print(player.name + ":" + str(player.chips))


# ********************** Testing *************************************''
def test():
    # Local hard coded test data
    players = [Player("1", 1), Player("2", 2), Player("3", 3)]

    # TODO Testing
    exit(0)


if __name__ == "__main__":
    lcr_program()
