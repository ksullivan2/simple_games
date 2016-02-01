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
    
    def change_game_state(self):
        self.ids["dice_layer"].roll_all_dice()
        if self.state == 0:
            self.ids["actionbutton"].text = "Roll again."
            self.state = 1
        elif self.state == 1:
            self.ids["actionbutton"].text = "Final roll."
            self.state = 2
        elif self.state == 2:
            self.ids["actionbutton"].text = "Confirm points and roll again."
            self.ids["actionbutton"].disabled = True
            #THIS IS WHAT YOU'RE WORKING ON
            self.show_scores_in_scorecard()
            self.ids["dice_layer"].pass_values_to_hand()
            self.state = 3
        elif self.state == 3: 
            self.ids["scorecard"].select_score()
            self.ids["actionbutton"].text = "Roll again."
            self.state = 1
    
    def unlock_action_button(self):
        self.ids["actionbutton"].disabled = False

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
        for dice in self.children:
            self.hand.append(dice.number)
        self.hand.sort()
        return self.hand

        

class RollButton(Button):
    def unlock(self):
        self.disabled = False
    
   

if __name__ == '__main__':
    YahtzeeApp().run()
