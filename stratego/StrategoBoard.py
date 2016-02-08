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
        print("change gamestate: " + str(self.gamestate))
        #0 is game setup
        #1 is player 1 move
        #2 is player 2 move
        if self.gamestate == 0:
            self.setup_to_place_pieces()
        elif self.gamestate == 1:
            self.setup_player_1_turn()
            # bind gamepieces.on_pos to something else?

    def debug_place_pieces(self):
        x = 6
        y = 0
        for piece in self.sidebar.children:
            piece.state = "down"
            self.board.grid[x][y].move_to_terrain()
            if y == 9:
                y = 0
                x += 1
            else:
                y += 1



    def setup_to_place_pieces(self):
        print("setup to place pieces")
        for square in self.board.children:
            if square.row in range(0,6):
                square.disabled = True
            else:
                square.disabled = False
            square.bind(on_press= square.move_to_terrain)
        for piece in self.sidebar.children:
            piece.bind(on_pos = self.pieces_are_all_placed)
            #this statement is currently doing nothing, apparently, the kivy is setting it

    def setup_player_1_turn(self):
        print("setup player 1 turn")
        for square in self.board.children:
            if square.occupied or not square.land:
                square.disabled = True
            else:
                square.disabled = False


    def pieces_are_all_placed(self, *args):
        for piece in self.sidebar.children:
            if piece.row is None:
                return False
        self.gamestate = 1
        return True






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