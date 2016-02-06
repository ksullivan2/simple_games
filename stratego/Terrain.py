from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.button import Button
from ResizeBehavior import *

class Terrain(Button):
    def __init__(self, row, col, land = True):
        self.row = row
        self.col = col
        self.id = str(self.row) + "," + str(self.col)
        self.land = land
        self.ratio = 1.
        super(Terrain,self).__init__()


    def get_background_image(self):
        if self.land:
            return "images/land.png"
        else:
            return "images/water.png"

    def place_piece(self, *args):
        for piece in self.parent.parent.parent.sidebar.children:
            if piece.state == "down":
                piece.pos = self.pos
                piece.state = "normal"

