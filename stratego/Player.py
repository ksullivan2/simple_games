from GamePiece import *

class Player():
    def __init__(self, color):
        self.color = color
        self.in_hand = None
        self.pieces = []

        for piecenumber in pieceamounts:
            for i in range(pieceamounts[piecenumber]):
                self.pieces.append((GamePiece(piecenumber, self.color)))

    def move_to_terrain(self, *args):
        for piece in self.parent.parent.parent.sidebar.children:
            if piece.state == "down" and not self.occupied:
                if piece.row is not None:
                    self.parent.grid[piece.row][piece.col].occupied = False
                piece.state = "normal"
                piece.col = self.col
                piece.row = self.row
                self.occupied = True
                piece.pos = self.pos
                break

