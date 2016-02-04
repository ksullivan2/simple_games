from kivy.uix.button import Button

class Terrain(Button):
    def __init__(self, row, col):
        self.row = row
        self.col = col
        super(Terrain,self).__init__()

