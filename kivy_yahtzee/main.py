from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.image import Image

from kivy.graphics import *

class YahtzeeApp(App):
    def build(self):
        return Dice()

class YahtzeeGame(BoxLayout):
    pass

class Dice(ToggleButtonBehavior, Image):
    def __init__(self, **kwargs):
        self.number = 2
        super(Dice, self).__init__(**kwargs)
        self.source = ("images/up_state/dice" + str(self.number) + ".gif")
        
    def on_state(self, widget, value):
        if value == "down":
            self.source = ("images/down_state/dice" + str(self.number) + ".gif")
        else:
           self.source = ("images/up_state/dice" + str(self.number) + ".gif")


if __name__ == '__main__':
    YahtzeeApp().run()
