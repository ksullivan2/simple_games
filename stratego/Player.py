from GamePiece import *

class Player():
    def __init__(self, color):
        self.color = color
        self.pieces = []
        self.in_hand = None

        for piecenumber in pieceamounts:
            for i in range(pieceamounts[piecenumber]):
                self.pieces.append((GamePiece(piecenumber, self.color)))

    def activate_player_pieces(self):
        for piece in self.pieces:
            piece.disabled = False

    def disable_player_pieces(self):
        for piece in self.pieces:
            piece.disabled = True

