from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from random import randint
from ResizeBehavior import *
from functools import partial
from Square import *
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




    def change_gamestate(self):
        print("change gamestate: " + str(self.gamestate))
        #0 is game setup
        #1 is move during game
        if self.gamestate == 0:
            self.player_start()

        elif self.gamestate == 1:
            self.setup_player_1_turn()

    def player_start(self):
        self.create_piece_widgets()
        self.setup_to_place_pieces()

    def create_piece_widgets(self):
        for piece, square in zip(self.activeplayer.pieces, self.sidebar.children):
            self.add_widget(piece)
            piece.spot = square
            piece.size = square.size
            square.occupied = True


    def place_in_hand(self, piece):
        self.activeplayer.in_hand = piece

        if self.gamestate == 1:
           self.board.highlight_valid_moves_during_game()

    def clear_hand(self):
        self.activeplayer.in_hand = None

        if self.gamestate == 1:
            self.clear_all_valid_markers()

    def debug_place_pieces(self):
        if self.activeplayer.color =="Red":
            x = 6
        else:
            x = 0
        y = 0
        templist = []
        for piece in self.activeplayer.pieces:
            templist.append(piece)
        while len(templist) > 0:
            piece = templist[randint(0,len(templist)-1)]
            self.activeplayer.in_hand = piece
            self.board.grid[x][y].move_to_square()
            templist.remove(piece)
            if y == 9:
                y = 0
                x += 1
            else:
                y += 1


    def disable_invalid_squares(self):
        for square in self.board.children:
            if square.valid:
                square.disabled = False
            else:
                square.disabled = True

    def clear_all_valid_markers(self):
        for square in self.board.children:
            square.disabled = True
            square.valid = False


    def pieces_placed_next_action(self):
        if self.activeplayer == self.player1:
            self.activeplayer = self.player2
            self.player_start()
        else:
            self.gamestate = 1
        return True

    def setup_to_place_pieces(self):
        if self.activeplayer.color == "Red":
            toprow = 6
            bottomrow = 9
        else:
            toprow = 0
            bottomrow = 3
        for square in self.board.children:
            if square.row in range(toprow, bottomrow+1):
                square.valid = True
            else:
                square.valid = False
        self.disable_invalid_squares()

        #move these
        self.board.player = self.activeplayer
        self.sidebar.player = self.activeplayer

    def setup_player_1_turn(self):
        #set up valid moves
        self.clear_all_valid_markers()

        #disable anything not in use
        for slot in self.sidebar.children:
            slot.disabled = True







