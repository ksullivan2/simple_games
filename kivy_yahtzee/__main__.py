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
    #4 is confirm
    #5 is ready for next roll
    
    def increment_game_state(self):
        if self.gamestate == 5:
            self.gamestate = 1
        else:
            self.gamestate += 1

    def change_game_state(self):
        scorecard = self.ids["scorecard"]
        #it's annoying to continually reference the whole thing....

        if self.gamestate == 0:
            self.ids["dicelayer"].disable_dice()
            scorecard.clear_scores()
            self.instructions = "Start your game!"
            self.ids["gameoverlabel"].text = "Game Over! Your score was: " + str(tally_score())

        if self.gamestate == 1:
            self.ids["dicelayer"].enable_dice()
            self.ids["dicelayer"].roll_all_dice()
            self.instructions = "Roll again."
            self.ids["gameoverlabel"].text = "Game State: " + str(self.gamestate)
            
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
            scorecard.disable_score_options()
            scorecard.select_score()
            if scorecard.check_if_complete() == False:
                self.instructions = "Roll your next hand."
            else:
                self.gamestate = 0

        

    def show_scores_in_scorecard(self):
        hand = self.ids["dicelayer"].pass_values_to_hand()
        possible_scores = check_for_points(hand)
        self.ids["scorecard"].show_score_options(possible_scores)

    def cheat(self):
        for option in self.ids["scorecard"].children:
            option.used = True

        

class DoTheThingButton(Button):
    def unlock(self):
        self.disabled = False
    

if __name__ == '__main__':
    YahtzeeApp().run()
