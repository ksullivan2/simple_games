from kivy.uix.button import Button

class Terrain(Button):
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