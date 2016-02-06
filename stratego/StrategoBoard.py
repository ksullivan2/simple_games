from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from ResizeBehavior import *
from functools import partial
from Terrain import *
from GamePiece import *



class StrategoWindow(FloatLayout):
    def __init__(self, **kwargs):
        super (StrategoWindow, self).__init__()
        self.board = self.ids["board"]
        self.sidebar = self.ids["sidebar"]

    def change_gamestate(self):
        #0 is game setup
        if self.gamestate == 0:
            self.setup_to_place_pieces()


    def setup_to_place_pieces(self):
        for square in self.board.children:
            if square.row in range(0,6):
                square.disabled = True
            else:
                square.disabled = False
            square.bind(on_press= square.place_piece)





class StrategoBoard(GridLayout):
    def __init__(self, **kwargs):
        self.grid = []
        super(StrategoBoard, self).__init__()
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


class Sidebar(GridLayout):
    def __init__(self, **kwargs):
        super(Sidebar, self).__init__()
        for piecenumber in pieceamounts:
            for i in range(pieceamounts[piecenumber]):
                self.add_widget(GamePiece(piecenumber, "Red"))