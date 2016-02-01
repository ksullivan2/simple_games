from kivy.app import App
from Dice import *
from ScoreCard import *
from ScoreCardBehavior import *



class YahtzeeApp(App):
    def build(self):
        return YahtzeeGame()

class YahtzeeGame(BoxLayout):
    pass

class DiceLayer(BoxLayout):
    roll_count = NumericProperty(0)

    def roll_all_dice(self):
        for dice in self.children:
             dice.roll()
             self.roll_count += 1
        

class RollButton(Button):
    pass
   

if __name__ == '__main__':
    YahtzeeApp().run()
