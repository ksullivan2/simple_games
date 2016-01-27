import random
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import NumericProperty, DictProperty
from kivy.uix.widget import Widget



score_types = ["Aces","Twos","Threes","Fours","Fives","Sixes",
         "Three of a Kind","Four of a Kind","Full House", "Small Straight",
         "Large Straight", "Chance", "Yahtzee", "Yahtzee Bonus"]


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
            score_card_dict[entry] = None
            self.add_widget(ScoreOption(text = entry, value = 0))
        score_card_dict = DictProperty
        #idea is that this will be used to store scores later...
    pass
 
