from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from ResizeBehavior import *
from functools import partial
from Terrain import *
from GamePiece import *



class Board(GridLayout):
    def __init__(self, **kwargs):
        self.grid = []
        super(Board, self).__init__()
        self.create_background()

    def create_background(self):
        for i in range(10):
            self.grid.append([])
            for j in range(10):
                if i in (4,5) and j in (2,3,6,7):
                    temp = Terrain(i,j, land=False)
                else:
                    temp = Terrain(i,j)
                self.grid[i].append(temp)
                self.add_widget(temp)


