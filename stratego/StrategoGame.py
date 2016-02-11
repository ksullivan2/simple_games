from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from ResizeBehavior import *
from functools import partial
from Terrain import *
from GamePiece import *
from Board import *
from Player import *


class StrategoGame(FloatLayout):
    def __init__(self, **kwargs):
        super (StrategoGame, self).__init__()
        self.board = self.ids["board"]
        self.sidebar = self.ids["sidebar"]
        self.player1 = Player("Red")
        self.player2 = Player("Blue")
        self.activeplayer = self.player1


    def create_piece_widgets(self):
        for piece, square in zip(self.activeplayer.pieces, self.sidebar.children):
            self.add_widget(piece)
            piece.spot = square
            piece.size = square.size
            square.occupied = True

    def change_gamestate(self):
        print("change gamestate: " + str(self.gamestate))
        #0 is game setup
        #1 is player 1 move
        #2 is player 2 move
        if self.gamestate == 0:
            self.create_piece_widgets()
            self.setup_to_place_pieces()

        elif self.gamestate == 1:
            self.setup_player_1_turn()
            # bind gamepieces.on_pos to something else?

    def place_in_hand(self, piece):
        self.activeplayer.in_hand = piece
        if self.gamestate == 1:
            self.board.highlight_valid_moves_during_game()



    def debug_place_pieces(self):
        x = 6
        y = 0
        for piece in self.activeplayer.pieces:
            self.activeplayer.in_hand = piece
            self.board.grid[x][y].move_to_square()
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
        self.board.player = self.activeplayer
        self.sidebar.player = self.activeplayer

    def setup_player_1_turn(self):
        print("setup player 1 turn")
        for square in self.board.children:
            if square.occupied or square.type != "land":
                square.disabled = True
            else:
                square.disabled = False
        for slot in self.sidebar.children:
            slot.disabled = True





