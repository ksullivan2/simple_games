from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import NumericProperty, DictProperty
from kivy.uix.relativelayout import RelativeLayout
from Dice import *
from yahtzee_definitions import *
#from kivy.graphics import *


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
    def __init__(self, text, value, **kwargs):
        super(ScoreOption, self).__init__()
        self.text = text
        self.value = value

class ScoreCard(BoxLayout):
    def __init__(self, **kwargs):
        super(ScoreCard,self).__init__()
        score_card_dict = {}
        for entry in score_types:
            score_card_dict[entry] = 1
            self.add_widget(ScoreOption(text = entry, value = 0))
        score_card_dict = DictProperty
        
    pass
    

if __name__ == '__main__':
    YahtzeeApp().run()
