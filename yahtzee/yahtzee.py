from yahtzee_definitions import *
from yahtzee_values import *
from yahtzee_human_actions import *


def initial_roll(player):
    '''rolls 5 dice'''
    for i in range(5):
        player.hand.append(roll_die())
    print_hand(player)



def turn(player):
    '''player rolls 3 times, then can choose where to put points'''
    initial_roll(player)
    re_roll_human(player)
    re_roll_human(player)
    choose_points_human(player)


def is_player_done(player):
    '''checks if all the slots in the player's card are full'''
    for key in player.score_card:
        if player.score_card[key] == None:
            return False
    return True
    

def game(player):
    '''while there are still slots in the player's card, they keep rolling'''
    while is_player_done(player) == False:
        turn(player)
        player.hand = []
    print("Your score is " + str(tally_score(player)))

#runner code
player1 = Player()
game(player1)
