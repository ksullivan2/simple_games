from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.image import Image
from random import randint
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty

class Dice(ToggleButtonBehavior, Image):
        
    def on_state(self, widget, value):
        if value == "down":
            self.source = ("images/down_state/dice" + str(self.number) + ".gif")
        else:
           self.source = ("images/up_state/dice" + str(self.number) + ".gif")

    def roll(self):
        if self.state != "down":
            self.number = randint(1,6)
            self.source = ("images/up_state/dice" + str(self.number) + ".gif")


class DiceLayer(BoxLayout):
    def __init__(self, **kwargs):
        super(DiceLayer,self).__init__()
        self.hand = []
        for i in range(5):
            self.add_widget(Dice())




    def roll_all_dice(self):
        for dice in self.children:
             dice.roll()

    def pass_values_to_hand(self):
        self.hand = []
        for dice in self.children:
            self.hand.append(dice.number)
        self.hand.sort()
        return self.hand

    def disable_dice(self):
        for dice in self.children:
            dice.disabled = True

    def enable_dice(self):
        for dice in self.children:
            dice.disabled = False
            dice.state = "normal"