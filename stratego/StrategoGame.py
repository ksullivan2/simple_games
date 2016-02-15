from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ObjectProperty
from kivy.graphics.instructions import *

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
        self.animation = Animation()

#gamestate actions

    def change_gamestate(self):
        #0 is game setup
        #1 is move during game
        if self.gamestate == 0:
            self.player_start()

        elif self.gamestate == 1:
            for slot in self.sidebar.children:
                slot.disabled = True


    def new_turn(self):
        self.swap_active_player()
        self.board.clear_all_valid_markers()


    def player_start(self):
        self.create_piece_widgets()
        self.setup_to_place_pieces()


    def create_piece_widgets(self):
        for piece, square in zip(self.activeplayer.pieces, self.sidebar.children):
            self.add_widget(piece)
            piece.spot = square
            piece.size = square.size
            square.occupied = True

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
        self.board.enable_valid_squares()


    def pieces_placed_next_action(self):
        if self.activeplayer == self.player1:
            self.swap_active_player()
            self.player_start()
        else:
            self.gamestate = 1
        return True


    def swap_active_player(self):
        self.activeplayer.disable_player_pieces()
        if self.activeplayer == self.player1:
            self.activeplayer = self.player2
        else:
            self.activeplayer = self.player1
        self.activeplayer.activate_player_pieces()
        print(self.activeplayer.color)



    def player_conflict(self, instance, idontknowwhythisishere, attacker, square):
        '''returns the winner of the conflict and destroys the loser'''
        if square.occupied is None:
            return

        defender = square.occupied
        winner = None
        loser = None

        #special cases first
        if defender.number == 0:
            pass
            #game over
        elif (attacker.number == 1 and defender.number == 10) or \
                (attacker.number == 3 and defender.number == 11) or \
                (attacker.number >= defender.number):
            winner = attacker
            loser = defender
        else:
            winner = defender
            loser = attacker

        #delete the losing piece, or move it to sidebar??
        loser.piece_death()
        return winne






#interacting with the "hand"
    def place_in_hand(self, piece):
        self.activeplayer.in_hand = piece

        if self.gamestate == 1:
            self.board.highlight_valid_moves_during_game()


    def clear_hand(self):
        self.activeplayer.in_hand = None

        if self.gamestate == 1:
            self.board.clear_all_valid_markers()


#debug functions

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


