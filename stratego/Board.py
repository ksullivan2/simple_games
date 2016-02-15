from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from ResizeBehavior import *
from functools import partial
from Square import *

from GamePiece import *
from Player import *



class Board(GridLayout):
    def __init__(self, **kwargs):
        self.grid = []

        super().__init__()


    #moving pieces around the board
    def move_to_square(self, square):
        if self.player.in_hand is not None:
            piece = self.player.in_hand

            #remove it from the previous spot and put it on new one
            piece.spot.occupied = None
            piece.spot = square

            #piece's animation
            piece.moveanim = Animation(pos = piece.spot.pos)
            piece.moveanim.bind(on_complete = partial(self.parent.player_conflict, attacker= piece, square= square))
            piece.moveanim.start(piece)

            #square and piece must reference each other
            square.occupied = piece
            piece.state = "normal"

        if self.parent.parent.gamestate == 1:
            self.parent.parent.new_turn()




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

    def highlight_valid_moves_during_game(self, *args):
        piece = self.player.in_hand

        if piece.max_spaces == 0:
            return

        self.find_x_moves(piece, 1)
        self.find_x_moves(piece, -1)
        self.find_y_moves(piece, 1)
        self.find_y_moves(piece, -1)
        self.enable_valid_squares()

    def clear_all_valid_markers(self):
        for square in self.children:
            square.disabled = True
            square.valid = False

    def enable_valid_squares(self):
        for square in self.children:
            if square.valid:
                square.disabled = False
                if square.occupied is not None and \
                    square.occupied.player_color != self.parent.parent.activeplayer.color:
                    square.occupied.disabled = False

            else:
                square.disabled = True

    def test_for_valid_square(self, square):
        if square.type == "land":
            if square.occupied is None or \
                square.occupied.color != self.player.color:
                return True
        return False

    def find_y_moves(self, piece, direction):
        '''direction: 1 is down, -1 is up. Goes through squares in that direction and marks the valid ones.
        Stops if it comes to an invalid square.'''
        for n in range(1, piece.max_spaces+1):
            newrow = piece.spot.row + n*direction
            if not 0 <= newrow <= 9:
                break
            else:
                possible_square = self.grid[newrow][piece.spot.col]
            if not self.test_for_valid_square(possible_square):
                   break
            else:
                possible_square.valid = True
                if possible_square.occupied is not None:
                    break


    def find_x_moves(self, piece, direction):
        '''direction: 1 is right, -1 is left. Goes through squares in that direction and marks the valid ones.
        Stops if it comes to an invalid square.'''
        for n in range(1, piece.max_spaces+1):
            newcol = piece.spot.col + n*direction
            if not 0 <= newcol <= 9:
                break
            else:
                possible_square = self.grid[piece.spot.row][newcol]
            if not self.test_for_valid_square(possible_square):
                   break
            else:
                possible_square.valid = True
                if possible_square.occupied is not None:
                    break



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
                temp.bind(occupied = self.pieces_are_all_placed)

    def pieces_are_all_placed(self, *args):
        for slot in self.children:
            if slot.occupied:
                return False
        self.parent.parent.pieces_placed_next_action()





