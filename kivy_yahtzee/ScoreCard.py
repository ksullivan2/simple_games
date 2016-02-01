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
        self.score_card_dict = {}
        for entry in score_types:
            self.score_card_dict[entry] = None
            self.add_widget(ScoreOption(id = entry))
        #idea is that this will be used to store scores later...

    def select_score(self):
        for option in self.children:
            if option.ids["button"].state == "down":
                option.ids["button"].disabled = True
            elif option.ids["button"].disabled == False:
                option.value = 0
    

    def show_score_options(self, choice_of_scores):
        for option in self.children:
            if option.id in choice_of_scores.keys() and option.ids["button"].disabled == False:
                option.value = choice_of_scores[option.id]



    





 
