from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image

class Terrain(ButtonBehavior, Image):
    def __init__(self, row, col, land = True):
        self.row = row
        self.col = col
        self.id = str(self.row) + "," + str(self.col)
        self.land = land
        super(Terrain,self).__init__()

    def get_background_image(self):
        if self.land:
            return "images/land.png"
        else:
            return "images/water.png"