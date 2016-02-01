from kivy.app import App
from Dice import *
from ScoreCard import *
from ScoreCardBehavior import *
from kivy.properties import NumericProperty




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
            self.state = 3
        elif self.state == 3:
            #choose score value here  
            self.ids["actionbutton"].text = "Roll again."
            self.state = 1
        
        


class DiceLayer(BoxLayout):  
    def roll_all_dice(self):
        for dice in self.children:
             dice.roll()
        

class RollButton(Button):
    pass
   

if __name__ == '__main__':
    YahtzeeApp().run()
