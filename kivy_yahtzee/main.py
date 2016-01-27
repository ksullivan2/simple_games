from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import NumericProperty, DictProperty
from kivy.uix.relativelayout import RelativeLayout
from Dice import *

from kivy.graphics import *

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
    
class ScoreOption(BoxLayout):
    pass

class ScoreCard(BoxLayout):
    pass
    

if __name__ == '__main__':
    YahtzeeApp().run()
