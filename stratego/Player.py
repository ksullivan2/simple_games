from GamePiece import *

class Player():
    def __init__(self):
        player.color = "Red"
        player.in_hand = None
        player.pieces = []

        for piecenumber in pieceamounts:
            for i in range(pieceamounts[piecenumber]):
                player.pieces.append((GamePiece(piecenumber, "Red"))

     def move_to_terrain(self, *args):
            #move from terrain class
