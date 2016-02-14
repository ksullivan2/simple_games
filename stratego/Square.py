from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.properties import BooleanProperty, ObjectProperty
from ResizeBehavior import *

class Square(Button):
    occupied = ObjectProperty(None, rebind = True, allownone=True)


    def __init__(self, row, col, type):
        self.row = row
        self.col = col
        self.id = str(self.row) + "," + str(self.col)
        self.type = type
        self.valid = False
        super().__init__()

    def get_ids(self):
        return self.id

    def get_background_image(self):
        return "images/" + self.type + ".png"

    def get_disabled_image(self):
        if self.type == "land":
            return "images/land_disabled.png"
        elif self.type == "water":
            return "images/water.png"
        else:
            return "atlas://data/images/defaulttheme/button_disabled"


    def on_press(self):
         #if self.occupied is None:
         self.parent.move_to_square(self)
         #else:
             #self.parent.player_conflict()













