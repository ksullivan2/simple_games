from kivy.app import App
from Dice import *
from ScoreCard import *



class YahtzeeApp(App):
    def build(self):
        return YahtzeeGame()

class YahtzeeGame(BoxLayout):
    pass

class DiceLayer(BoxLayout):
    def roll_all_dice(self):
        for dice in self.children:
             dice.roll()

class RollButton(Button):
    pass
   

if __name__ == '__main__':
    YahtzeeApp().run()
