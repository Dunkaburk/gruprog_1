# /*
#  * The Pig game
#  * See http://en.wikipedia.org/wiki/Pig_%28dice_game%29
#  *
#  */

import random

def run():
    win_points = 30  # Points to win 
    aborted = False
    players = get_players() 
    welcome_msg(win_points)
    status_msg(players)
    current = random.choice(players)  # Randomly selects a player from players

    # Game logic, using small step, functional decomposition

    while True:

        if current.roundPts+current.totalPts >= win_points:  # Checks if the current points equal or exceed points required to win.
            break
        
        p_answer = get_player_choice(players, current)
        player_roll = 0
        if p_answer.lower() == "r": # If player answered "r" a dice is rolled and added to their roundPts.
            player_roll = roll(players, current)

        elif p_answer.lower() == "n":# If player answered "n" their roundPts are added to their totalPts and the next turn begins.
            current = next_turn(players, current)
            
        elif p_answer.lower() == "q": # If player answered "q" the game is aborted
            aborted = True
            break
        else: # Error validation, if player enters none of the above they are prompted to retry.
            print("Incorrect input! Type r to roll, n to hold or q to quit")



        if player_roll == 1: # If player rolled a 1, their roundPts are set to 0 and the next turn starts.
            current.roundPts = 0 
            current = next_player(players, get_player_index(players, current))

        
    game_over_msg(current, aborted)


class Player:

    def __init__(self, name=''):
        self.name = name  # default ''
        self.totalPts = 0  # Total points for all rounds
        self.roundPts = 0  # Points for a single round


# ---- Game logic methods --------------
# 
#
def roll(players, current):

    player_roll = random.randrange(1, 6)
    players[get_player_index(players, current)].roundPts += player_roll
    round_msg(player_roll, current)

    return player_roll


def get_player_index(players, current): # Takes players and current as arguments and returns at which index of the list players the current player is at.
    for i in players:
        if(i == current):
            current_index = players.index(i)
            return current_index

def next_turn(players, current):
    current.totalPts += current.roundPts
    current.roundPts = 0

    print("Your total points are", current.totalPts)
    current = next_player(players, get_player_index(players, current))
    return current



def next_player(players, player_index): # Takes the list players and current player index as arguments and sets current player to equal the next element in the list players, thereby setting current to the next player's turn.
    if player_index + 1 == len(players):
        current = players[player_index - (len(players)-1)]
    else:
        current = players[player_index + 1]

    return current


def get_players(): # Prompts the user to enter wanted amount of players and enter their names. If user enters an invalid input they are prompted to retry. Returns players as a list. 
    players = []
    p_name = ""
    try:
        number_of_players = int(input("Please enter the amount of players\n"))
        print("\n")
        i = 0
        while number_of_players <= 0:
            print("Invalid number of players, please retry")
            number_of_players = int(input("Please enter the amount of players\n"))

        while i < number_of_players:
            i += 1
            p_name = input("Please enter the name of player " + str(i) + "\n")

            print("\n")
            players.append(Player(name=p_name))
        
                
        return players

    except ValueError:
        print("Invalid number of players or player names, please try again")
        return get_players()


# ---- IO Methods --------------
def welcome_msg(win_pts):
    print("Welcome to PIG!")
    print("First player to get " + str(win_pts) + " points will win!")
    print("Commands are: r = roll , n = next, q = quit")


def status_msg(the_players):
    print("Points: ")
    for player in the_players:
        print("\n\t" + player.name + " = " + str(player.totalPts) + " ")


def round_msg(result, current):
    if result > 1:
        point = current.roundPts
        print("Got " + str(result) + " running total are " + str(point))
    else:
        print("Got 1 lost it all!")



def game_over_msg(player, is_aborted):
    if is_aborted:
        print("Aborted")
    else:
        print("Game over! Winner is player " + player.name + " with "
              + str(player.totalPts + player.roundPts) + " points")


def get_player_choice(player, current):
    print("\n" + str(current.name) + ", You're up!")
    p_answer = input()
    return p_answer





    

    

# ----- Testing -----------------
# Here you run your tests i.e. call your game logic methods
# to see that they really work (IO methods not tested here)
def test():

    win_points = 30  
    aborted = False
    test_players = [Player(), Player(), Player()]
    current = random.choice(test_players)

    # This is hard coded test data
    # An array of (no name) Players (probably don't need any name to test)
    
    # TODO Use for testing of logical methods (i.e. non-IO methods




if __name__ == "__main__":
    run()
    #test()
