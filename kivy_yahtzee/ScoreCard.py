import random
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import NumericProperty, DictProperty, StringProperty
from kivy.uix.widget import Widget



score_types = ["Aces","Twos","Threes","Fours","Fives","Sixes",
         "Three of a Kind","Four of a Kind","Full House", "Small Straight",
         "Large Straight", "Chance", "Yahtzee", "Yahtzee Bonus"]



    
class ScoreOption(BoxLayout):
    text = StringProperty("default")
    value = NumericProperty(0)

class ScoreCard(BoxLayout):
    def __init__(self, **kwargs):
        super(ScoreCard,self).__init__()
        self.score_card_dict = DictProperty({})
        for entry in score_types:
            #self.score_card_dict.add(entry: None)
            self.add_widget(ScoreOption(text = entry))
        #for key in score_card_dict.keys():
            #print(score_card_dict)
        #idea is that this will be used to store scores later...
    pass
 
