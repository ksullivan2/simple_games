from kivy.app import App
from Dice import *
from ScoreCard import *
#from ScoreCardBehavior import *
from kivy.properties import NumericProperty, ListProperty
from ValueChecking import *




class YahtzeeApp(App):
    def build(self):
        return YahtzeeGame()

class YahtzeeGame(BoxLayout):
    state = NumericProperty(0)
    #0 is ready for first roll, first turn only
    #1 is ready for 2nd roll
    #2 is ready for final roll
    #3 is dice set, choose score value
    #4 is score chosen, ready for roll
    
    def change_game_state(self):
        
        if self.state == 0:
            self.ids["dice_layer"].roll_all_dice()
            self.ids["actionbutton"].text = "Roll again."
            self.state = 1
        elif self.state == 1:
            self.ids["dice_layer"].roll_all_dice()
            self.ids["actionbutton"].text = "Final roll."
            self.state = 2
        elif self.state == 2:
            self.ids["dice_layer"].roll_all_dice()
            self.ids["actionbutton"].text = "Choose where to put your points."
            self.ids["actionbutton"].disabled = True
            self.ids["dice_layer"].disable_dice_roll()
            self.show_scores_in_scorecard()
        elif self.state == 3:
           self.ids["actionbutton"].text = "Confirm points and roll your next hand." 
           self.state = 4
        elif self.state == 4: 
            self.ids["scorecard"].select_score()
            self.ids["dice_layer"].enable_dice_roll()
            self.ids["dice_layer"].roll_all_dice()
            self.ids["actionbutton"].text = "Roll again."
            self.state = 1
        
    
    def a_score_is_selected(self):
        self.ids["actionbutton"].disabled = False
        self.state = 3
        self.change_game_state()

    def show_scores_in_scorecard(self):
        hand = self.ids["dice_layer"].pass_values_to_hand()
        possible_scores = check_for_points(hand)
        #choice_of_scores = check_points_against_score_card(self.ids["scorecard"].score_card_dict, possible_scores)
        self.ids["scorecard"].show_score_options(possible_scores)
        


        


class DiceLayer(BoxLayout):  
    hand = ListProperty([])

    def roll_all_dice(self):
        for dice in self.children:
             dice.roll()

    def pass_values_to_hand(self):
        self.hand = []
        for dice in self.children:
            self.hand.append(dice.number)
        self.hand.sort()
        return self.hand

    def disable_dice_roll(self):
        for dice in self.children:
            dice.disabled = True

    def enable_dice_roll(self):
        for dice in self.children:
            dice.disabled = False
            dice.state = "normal"

        

class RollButton(Button):
    def unlock(self):
        self.disabled = False
    
   

if __name__ == '__main__':
    YahtzeeApp().run()
