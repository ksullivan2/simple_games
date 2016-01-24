from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.image import Image
from random import randint

class Dice(ToggleButtonBehavior, Image):
    def __init__(self, **kwargs):
        self.number = 6
        super(Dice, self).__init__(**kwargs)
        self.source = ("images/up_state/dice" + str(self.number) + ".gif")
        
    def on_state(self, widget, value):
        if value == "down":
            self.source = ("images/down_state/dice" + str(self.number) + ".gif")
        else:
           self.source = ("images/up_state/dice" + str(self.number) + ".gif")

    def roll(self):
        if self.state != "down":
            self.number = randint(1,6)
            self.source = ("images/up_state/dice" + str(self.number) + ".gif")
