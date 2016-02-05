from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from ResizeBehavior import *


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

amounts = {0: 1,
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


class GamePiece(ToggleButtonBehavior, Image):
    def __init__(self, number, **kwargs):
        self.number = number
        self.ratio = 1.
        super(GamePiece, self).__init__()

    def get_name(self):
        return names[self.number]




class InitialPieces(GridLayout):
    def __init__(self, **kwargs):
        super(InitialPieces, self).__init__()
        for piecenumber in amounts:
            for i in range(amounts[piecenumber]):
                self.add_widget(GamePiece(piecenumber))


