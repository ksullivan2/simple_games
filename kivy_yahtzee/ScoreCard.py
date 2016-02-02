#import random
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import NumericProperty, DictProperty, \
                            StringProperty, ObjectProperty
from kivy.uix.widget import Widget
from ValueChecking import score_types
from kivy.utils import escape_markup





    
class ScoreOption(BoxLayout):
    text = StringProperty("default")
    value = NumericProperty(0)

    def italicize_text(self):
        for widget in self.children:
            widget.markup = True
            widget.text = "[i]" + widget.text + "[/i]"



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

            if option.id == "Yahtzee Bonus":
                #I thought I could use self.ids["Yahtzee Bonus"] instead of self.children[1] but it won't work
                if self.children[1].used == True and self.children[1].value != 0:
                    if choice_of_scores["Yahtzee Bonus"] != 0:
                        option.disabled = False
                else:
                    option.disabled = True

            if option.id in choice_of_scores.keys() and option.disabled == False:
                option.value += choice_of_scores[option.id]


    def disable_score_options(self):
        for option in self.children:
            option.disabled = True

    def enable_score_options(self):
        for option in self.children:
            if option.used == False:
                option.disabled = False


    def check_if_complete(self):
        for option in self.children:
            if option.id != "Yahtzee Bonus" and option.used == False:
                return False
        return True

    def clear_scores(self):
        '''clears out the score card for a new game'''
        for option in self.children:
            option.value = 0
            option.used = False
            option.disabled = True
            option.ids["button"].text = option.id




    def tally_score(self):
        '''tallies the score card'''
        total = 0
        first_half_total = 0
        for option in self.children:
            total += option.value
            if option.id in ["Aces","Twos","Threes","Fours","Fives","Sixes"]:
                first_half_total += option.value
        if first_half_total >= 63:
            total += 35
        return total

 
