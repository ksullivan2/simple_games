import random

score_types = ["aces","twos","threes","fours","fives","sixes",
         "three_of_a_kind","four_of_a_kind","full_house", "small_straight",
         "large_straight", "chance", "yahtzee", "yahtzee_bonus"]


class Player:
    def __init__(self):
        self.hand = []
        self.score_card = {key: None for key in score_types}
        self.int = 5



def roll_die():
    return random.randint(1,6)

