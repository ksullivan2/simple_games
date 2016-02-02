from kivy.app import App
from Dice import *
from ScoreCard import *
#from ScoreCardBehavior import *
from kivy.properties import NumericProperty
from ValueChecking import *




class YahtzeeApp(App):
    def build(self):
        return YahtzeeGame()
        pass

class YahtzeeGame(BoxLayout):
    gamestate = NumericProperty(0)
    #0 is new game
    #1 is rolled once
    #2 is rolled twice
    #3 is choose your value
    #4 is confirm and re-start rolling
    
    def increment_game_state(self):
        if self.gamestate == 5:
            self.gamestate = 1
        else:
            self.gamestate += 1

    def change_game_state(self):
        if self.gamestate == 1:
            self.ids["dicelayer"].enable_dice()
            self.ids["dicelayer"].roll_all_dice()
            self.instructions = "Roll again."
            
        elif self.gamestate == 2:
            self.ids["dicelayer"].roll_all_dice()
            self.instructions = "Final roll."
            
        elif self.gamestate == 3:
            self.ids["dicelayer"].roll_all_dice()
            self.instructions = "Choose where to put your points."
            self.ids["actionbutton"].disabled = True
            self.ids["scorecard"].enable_score_options()
            self.ids["dicelayer"].disable_dice()
            self.show_scores_in_scorecard()

        elif self.gamestate == 4:
           self.instructions = "Confirm points?" 
           self.ids["actionbutton"].disabled = False

        elif self.gamestate == 5:
            self.ids["scorecard"].disable_score_options()
            self.ids["scorecard"].select_score()
            self.instructions = "Roll your next hand."


            
        

    def show_scores_in_scorecard(self):
        hand = self.ids["dicelayer"].pass_values_to_hand()
        possible_scores = check_for_points(hand)
        #choice_of_scores = check_points_against_score_card(self.ids["scorecard"].score_card_dict, possible_scores)
        self.ids["scorecard"].show_score_options(possible_scores)
        


        








        

class DoTheThingButton(Button):
    def unlock(self):
        self.disabled = False
    
   

if __name__ == '__main__':
    YahtzeeApp().run()
