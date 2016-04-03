from yahtzee_definitions import *
from yahtzee_values import *



def print_hand(player):
    '''sorts and prints human-readable hand'''
    player.hand.sort()
    print("Your hand is " + str(player.hand))
    
def print_score_card(card):
    '''prints human readable card and returns the indices it was able to print
    so that when humans need to refer by #, they can'''
    #adding this array for use in the choose_points_human method
    indices_array = []
    for index, key in enumerate(score_types):
        try:
            print(str(index+1) + ". " + key + ": " + str(card[key]))
            indices_array.append(index+1)
        except KeyError:
            pass
    return indices_array

def get_indices():
    '''allows humans to choose which dice to exchange'''
    valid = False
    indices_to_exchange = []

    while valid == False:
        try:
            input_value = input()
            if input_value == "all":
                indices_to_exchange = [1,2,3,4,5]
                valid = True
                break
            if input_value == "end":
                valid = True
                break
            if input_value == "undo" and len(indices_to_exchange) > 0:
                indices_to_exchange.pop()
            elif int(input_value) in range(1,6) and int(input_value) not in indices_to_exchange:
                indices_to_exchange.append(int(input_value))
                if len(indices_to_exchange) == 5:
                    valid = True
                    break
            else:
                print("That was not a valid response.")
            print("You are exchanging indices " + str(indices_to_exchange) + " any others?")
        except (ValueError):
            print("ValueError, try again.")
    return indices_to_exchange


def re_roll_human(player):
    '''allows humans to re-roll certain dice'''
    print("Which dice would you like to re-roll? \nType 1-5 or \"all.\" Use \"end\" to end or \"undo\" to take back a number.")
    indices_to_exchange = get_indices()
    for index in indices_to_exchange:
        player.hand[index-1] = roll_die()
    print_hand(player)


def choose_points_human(player):
    '''allows humans to choose where to allot their points'''
    possible_scores = check_for_points(player.hand)
    options = check_points_against_score_card(player, possible_scores)
    options_indices = print_score_card(options)
    
    valid = False
    while valid == False:
        try:
            input_value = int(input("Where would you like to put these points? Type a number."))
            if input_value in options_indices:
                player.score_card[score_types[input_value-1]] = options[score_types[input_value-1]]
                valid = True
            else:
                print("That was not in range. Try again.")
        except ValueError:
            print("That was not a valid index.")
                
