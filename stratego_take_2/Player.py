from GamePiece import *
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty

class Player(Widget):
    pieces_left_to_be_placed = NumericProperty(0)

    def __init__(self, color):
        self.color = color
        self.pieces = []


        for piecenumber in pieceamounts:
            for i in range(pieceamounts[piecenumber]):
                self.pieces.append((GamePiece(piecenumber, self.color)))


    def activate_player_pieces(self):
        for piece in self.pieces:
            if not piece.dead:
                piece.disabled = False

    def disable_player_pieces(self):
        for piece in self.pieces:
            piece.disabled = True

