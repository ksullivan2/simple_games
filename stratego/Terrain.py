from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.properties import BooleanProperty
from ResizeBehavior import *

class Square(Button):
    def __init__(self, row, col, type):
        self.row = row
        self.col = col
        self.id = str(self.row) + "," + str(self.col)
        self.type = type
        self.occupied = BooleanProperty(False)
        super().__init__()

    def get_ids(self):
        return self.id

    def get_background_image(self):
        return "images/" + self.type + ".png"


    def move_to_square(self):
        if self.parent.player.in_hand is not None:
            piece = self.parent.player.in_hand
            self.parent.player.in_hand = None

            #remove it from the previous spot
            piece.spot.occupied = False

            #set attributes of new spot
            self.occupied = True
            piece.state = "normal"
            piece.spot = self







