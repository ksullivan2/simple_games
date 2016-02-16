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
    #events = ObjectProperty(EventHandler())


    def __init__(self, **kwargs):
        super (StrategoGame, self).__init__()
        self.events = EventHandlers(self)
        self.board = self.ids["board"]
        self.sidebar = self.ids["sidebar"]
        self.player1 = Player("Red")
        self.player2 = Player("Blue")
        self.activeplayer = self.player1
        self.animation = Animation()


#gamestate actions

    def change_gamestate(self, newstate):
        print(self.gamestate, newstate)
        self.gamestate = newstate

        '''
        activities associated with leaving the current state
        change the current status to the new status
        activities associated with entering the new state
        '''
        
        #-1 is new window
        #0 is game setup, no piece selected
        #1 is game setup, piece selected
        #2 is all pieces placed
        #3 is gameplay, no piece selected
        #4 is gaemplay, piece selected
        #5 is player conflict

        if self.gamestate == 0:
            self.player_start()

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
        print(self.activeplayer.color)


#interacting with the "hand"
    def place_in_hand(self, piece):
        self.activeplayer.in_hand = piece
        print(self.activeplayer.in_hand.number)

        if self.gamestate == 1:
            self.board.highlight_valid_moves_during_game()


    def clear_hand(self):
        self.activeplayer.in_hand = None

        if self.gamestate == 1:
            self.board.clear_all_valid_markers()

#creating players

    def player_start(self):
        self.create_piece_widgets()
        self.setup_gamestate_0()


    def create_piece_widgets(self):
        for piece, square in zip(self.activeplayer.pieces, self.sidebar.children):
            self.add_widget(piece)
            piece.spot = square
            piece.pos = piece.spot.pos
            piece.size = square.size
            piece.events = self.events
            square.occupied = True

    def setup_gamestate_0(self):
        '''activates the appropriate rows for each player'''
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
        #self.board.enable_valid_squares()
        self.activeplayer.bind(pieces_on_board = self.pieces_are_all_placed)

    def pieces_are_all_placed(self, *args):
        if self.activeplayer.pieces_on_board != 40:
            return

        print("pieces placed")
        if self.activeplayer == self.player1:
            self.swap_active_player()
            self.player_start()
        else:
            self.gamestate = 1




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


