from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton




class GamePiece(ToggleButton):
    '''def __init__(self, number, **kwargs):
        self.number = number
        super(GamePiece, self).__init__()'''


    def get_name(self):
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
        return names[self.number]

