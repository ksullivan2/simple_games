import random
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import NumericProperty, DictProperty, \
                            StringProperty, ObjectProperty
from kivy.uix.widget import Widget
from ValueChecking import score_types





    
class ScoreOption(BoxLayout):
    text = StringProperty("default")
    value = NumericProperty(0)
    




class ScoreCard(BoxLayout):
    def __init__(self, **kwargs):
        super(ScoreCard,self).__init__()
        for entry in score_types:
            self.add_widget(ScoreOption(id = entry))

    def select_score(self):
        for option in self.children:
            if option.ids["button"].state == "down":
                option.used = True
            elif option.used == False:
                option.value = 0
    

    def show_score_options(self, choice_of_scores):
        for option in self.children:
            if option.id in choice_of_scores.keys() and option.ids["button"].disabled == False:
                option.value = choice_of_scores[option.id]

    def disable_score_options(self):
        for option in self.children:
            option.ids['button'].disabled = True

    def enable_score_options(self):
        for option in self.children:
            if option.used == False:
                option.ids['button'].disabled = False



    





 
