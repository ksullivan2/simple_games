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
        for piece, spot in zip(self.activeplayer.pieces, self.sidebar.children):
            print(spot.pos)
            piece.size_hint = (None, None)
            piece.size = spot.size

            piece.pos = spot.pos
            self.add_widget(piece)


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
        for piece in self.sidebar.children:
            piece.bind(on_press = partial(self.highlight_valid_moves,piece))


    def pieces_are_all_placed(self, *args):
        for piece in self.sidebar.children:
            if piece.row is None:
                return False
        self.gamestate = 1
        return True


    def highlight_valid_moves(self, piece, *args):
        print("highlight valid moves")
        self.find_x_moves(piece, 1)
        self.find_x_moves(piece, -1)
        self.find_y_moves(piece, 1)
        self.find_y_moves(piece, -1)

    def find_x_moves(self, piece, direction):
        '''direction: 1 is right, -1 is left. Goes through squares in that direction and marks the valid ones.
        Stops if it comes to an invalid square.'''
        for n in range(piece.max_spaces):
            if 0 <= (piece.row + n*direction) <= 9:
                print('had a valid range')
                possible_square = self.board.grid[piece.row + n*direction][piece.col]
            else:
                print('out of range')
                break
            if possible_square.occupied or not possible_square.land:
                (print(str(possible_square.row)+"," + str(possible_square.col) + " stopped"))
                break
            else:
                print(str(possible_square.row)+"," + str(possible_square.col) + " stopped") + " valid"
                possible_square.disabled = True
                #disabled is for testing purposes, will need to figure out something better

    def find_y_moves(self, piece, direction):
        '''direction: 1 is right, -1 is left. Goes through squares in that direction and marks the valid ones.
        Stops if it comes to an invalid square.'''
        for n in range(piece.max_spaces):
            if 0 <= (piece.col + n*direction) <= 9:
                possible_square = self.board.grid[piece.row][piece.col +n*direction]
            else:
                break
            if possible_square.occupied or not possible_square.land:
                break
            else:
                possible_square.disabled = True
                #disabled is for testing purposes, will need to figure out something better


