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
from GameState import GameState


class StrategoGame(FloatLayout):
    def __init__(self, **kwargs):
        super (StrategoGame, self).__init__()
        #create players
        self.player1 = Player("Red")
        self.player2 = Player("Blue")

        #create aliases for children widgets
        self.board = self.ids["board"]
        self.sidebar = self.ids["sidebar"]

        #gamestatus
        self.activeplayer = self.player1
        self.pieceinhand = None
        self.gamestate = GameState.player_setup

        #set up event handlers for all relevant widgets
        self.eventsobject = EventsMethods(self)
        self.board.eventsobject = self.eventsobject
        self.sidebar.eventsobject = self.eventsobject

        #board also needs to know the active player
        self.board.activeplayer = self.activeplayer





#gamestate actions

    def change_gamestate(self, newstate):
        print("swap", self.gamestate, "to", newstate)
        self.gamestate = newstate

        if self.gamestate == GameState.start:
            self.player_start()
            self.board.highlight_valid_game_setup_rows()
            self.change_gamestate(GameState.setup_no_piece)

        elif self.gamestate == GameState.setup_no_piece:
            pass

        elif self.gamestate == GameState.pieces_placed:
            for slot in self.sidebar.children:
                slot.disabled = True
            self.change_gamestate(GameState.gameplay_no_piece)
            self.swap_active_player()


        elif self.gamestate == GameState.gameplay_no_piece:
            self.board.clear_all_valid_markers()


        elif self.gamestate == GameState.game_selected_piece:
            self.board.highlight_valid_moves_during_game(self.pieceinhand)




    def swap_active_player(self):
        self.activeplayer.disable_player_pieces()
        if self.activeplayer == self.player1:
            self.activeplayer = self.player2
        else:
            self.activeplayer = self.player1
        #make sure the board knows the new player too...
        self.board.activeplayer = self.activeplayer

        self.activeplayer.activate_player_pieces()
        print("swap activeplayer to " + self.activeplayer.color)


#interacting with the "hand"
    def place_in_hand(self, piece):
        self.pieceinhand = piece


    def clear_hand(self):
        self.pieceinhand = None


#moving pieces around the board

    def update_pieces_left_to_be_placed(self, square):
        if self.pieceinhand.spot.type != "sideboard":
            if square.type == "sideboard":
                self.activeplayer.pieces_left_to_be_placed += 1
            else:
                self.activeplayer.pieces_left_to_be_placed -=1

    def move_to_square(self, square, on_complete=None):
        piece = self.pieceinhand

        #remove it from the previous spot and put it on new one
        piece.spot.occupied = None

        #piece's animation
        piece.moveanim = Animation(pos = square.pos)
        if on_complete:
            piece.moveanim.bind(on_complete = partial(on_complete, self, square))
        piece.moveanim.start(piece)

        #this is necessary since this method is also used before player conflict
        if square.occupied is None:
            self.officially_place_on_square(square, piece)

    def officially_place_on_square(self, square, piece):
        piece.spot = square
        square.occupied = piece
        piece.state = "normal"



#creating players & pieces

    def player_start(self):
        '''creates the gamepieces for each player'''

        #initializes the count of how many pieces are left to be placed
        #which will count down to 0
        self.activeplayer.bind(pieces_left_to_be_placed = self.eventsobject.piece_placed)

        for piece, square in zip(self.activeplayer.pieces, self.sidebar.children):
            self.add_widget(piece)
            piece.spot = square
            piece.pos = piece.spot.pos
            piece.size = square.size
            piece.eventsobject = self.eventsobject
            square.occupied = True



#boolean helper functions
    def pieces_are_all_placed(self, *args):
        if self.activeplayer.pieces_left_to_be_placed > 0:
            return False

        print("pieces placed")
        return True

    def piece_belongs_to_activeplayer(self, piece):
        if piece.player_color == self.activeplayer.color:
            return True
        return False


#conflict

    def player_conflict(self, square):
        '''returns the winner of the conflict and destroys the loser'''
        attacker = self.pieceinhand
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
            print("attacker wins")
            winner = attacker
            loser = defender
        else:
            print("defender wins")
            winner = defender
            loser = attacker

        #delete the losing piece, or move it to sidebar??
        self.piece_death(loser)

        self.officially_place_on_square(square, winner)

    def piece_death(self, piece):
        piece.dead = True
        self.pieceinhand = piece
        for slot in self.sidebar.children:
            if slot.occupied is None:
                self.move_to_square(slot)
                piece.disabled = True
                break
        #there are not enough slots....





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
            self.pieceinhand = piece
            self.move_to_square(self.board.grid[x][y])
            templist.remove(piece)
            self.activeplayer.pieces_left_to_be_placed -= 1
            if y == 9:
                y = 0
                x += 1
            else:
                y += 1


