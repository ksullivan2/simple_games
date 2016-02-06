from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from ResizeBehavior import *





class GamePiece(ToggleButton):
    def __init__(self, number, color, **kwargs):
        self.number = number
        self.player_color = color
        self.ratio = 1.
        self.col = None
        self.row = None
        super(GamePiece, self).__init__()

    def get_name(self):
        return names[self.number]



names = {0: "Flag",
         1: "Spy",
         2: "Scout",
         3: "Miner",
         4: "Sergeant",
         5: "Lieutenant",
         6: "Captain",
         7: "Major",
         8: "Colonel",
         9: "General",
         10: "Marshal",
         11: "Bomb"}

pieceamounts = {0: 1,
           1: 1,
           2: 8,
           3: 5,
           4: 4,
           5: 4,
           6: 4,
           7: 3,
           8: 2,
           9: 1,
           10: 1,
           11: 6}

