from yahtzee_definitions import *
from yahtzee_values import *


#this should be changed later
def initial_roll(player):
    '''rolls 5 dice'''
    for i in range(5):
        player.hand.append(roll_die())
    player.hand.sort()
    


computer = Player()
initial_roll(computer)

computer.score_card["fives"] = 5


choice_of_scores = check_points_against_score_card(computer, check_for_points(computer.hand))
print(choice_of_scores)                                                

def choose_points_computer(player, choice_of_scores):
    key = max(choice_of_scores, key=choice_of_scores.get)
    player.score_card[key] = choice_of_scores[key]
    

choose_points_computer(computer, choice_of_scores)



