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
from EventHandler import *


class StrategoGame(FloatLayout):
    def __init__(self, **kwargs):
        super (StrategoGame, self).__init__()
        #initialize
        self.events = EventHandlers(self)
        self.board = self.ids["board"]
        self.sidebar = self.ids["sidebar"]
        self.player1 = Player("Red")
        self.player2 = Player("Blue")

        #gamestatus
        self.activeplayer = self.player1
        self.pieceinhand = None
        self.gamestate = -1



#gamestate actions

    def change_gamestate(self, newstate):
        print("swap", self.gamestate, "to", newstate)
        self.gamestate = newstate

        if self.gamestate == 0:
            self.player_start()
            self.board.highlight_valid_game_setup_rows(self.activeplayer)


        elif self.gamestate == 1:
            for slot in self.sidebar.children:
                slot.disabled = True
            self.swap_active_player()



    def new_turn(self):
        print("new turn")
        self.swap_active_player()
        self.board.clear_all_valid_markers()


    def swap_active_player(self):
        self.activeplayer.disable_player_pieces()
        if self.activeplayer == self.player1:
            self.activeplayer = self.player2
        else:
            self.activeplayer = self.player1
        self.activeplayer.activate_player_pieces()
        print("swap activeplayer to " + self.activeplayer.color)


#interacting with the "hand"
    def place_in_hand(self, piece):
        self.pieceinhand = piece


    def clear_hand(self):
        self.pieceinhand = None

        #if self.gamestate == 1:
            #self.board.clear_all_valid_markers()



#creating players

    def player_start(self):
        '''creates the gamepieces for each player'''

        #initializes the count of how many pieces are left to be placed
        self.activeplayer.bind(pieces_left_to_be_placed = self.pieces_are_all_placed)

        for piece, square in zip(self.activeplayer.pieces, self.sidebar.children):
            self.add_widget(piece)
            piece.spot = square
            piece.pos = piece.spot.pos
            piece.size = square.size
            piece.events = self.events
            square.occupied = True







#boolean helper functions
    def pieces_are_all_placed(self, *args):
        if self.activeplayer.pieces_left_to_be_placed > 0:
            return False

        print("pieces placed")
        return True




    def piece_belongs_to_activeplayer(self, piece):
        if piece.player_color == activeplayer.color:
            return True
        return False


#gameplay actions

    def player_conflict(self, instance, idontknowwhythisishere, square, attacker):
        '''returns the winner of the conflict and destroys the loser'''
        if square.occupied is None:
            self.board.officially_place_on_square(square, attacker)
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

        self.board.officially_place_on_square(square, winner)







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
            self.board.move_to_square(self.board.grid[x][y])
            templist.remove(piece)
            if y == 9:
                y = 0
                x += 1
            else:
                y += 1


