from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from ResizeBehavior import *
from functools import partial
from Terrain import *
from GamePiece import *
from Player import *



class Board(GridLayout):
    def __init__(self, **kwargs):
        self.grid = []
        self.player = Player("Red")
        #change this to reference game.activeplayer later....
        super().__init__()


class GameBoard(Board):
    def __init__(self, **kwargs):
        super().__init__()
        self.cols = 10
        self.create_background()

    def create_background(self):
        for i in range(10):
            self.grid.append([])
            for j in range(10):
                if i in (4,5) and j in (2,3,6,7):
                    temp = Square(i,j, "water")
                else:
                    temp = Square(i,j, "land")
                self.grid[i].append(temp)
                self.add_widget(temp)


class SideBoard(Board):
    def __init__(self, **kwargs):
        super().__init__()
        #self.player = super.player
        self.cols = 4
        self.create_slots()

    def create_slots(self):
        for i in range(10):
            self.grid.append([])
            for j in range(4):
                temp = Square(i,j, "sideboard")
                self.grid[i].append(temp)
                self.add_widget(temp)

