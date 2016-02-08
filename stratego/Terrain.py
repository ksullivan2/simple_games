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
        self.occupied = False
        super(Terrain,self).__init__()

    def get_ids(self):
        return self.id

    def get_background_image(self):
        if self.land:
            return "images/land.png"
        else:
            return "images/water.png"

    def move_to_terrain(self, *args):
        for piece in self.parent.parent.parent.sidebar.children:
            if piece.state == "down" and not self.occupied:
                if piece.row is not None:
                    self.parent.grid[piece.row][piece.col].occupied = False
                piece.state = "normal"
                piece.col = self.col
                piece.row = self.row
                self.occupied = True
                piece.pos = self.pos
                break



