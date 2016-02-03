from kivy.uix.boxlayout import BoxLayout

class GamePiece(BoxLayout):
    def __init__(self, number, **kwargs):
        super(GamePiece,self).__init__()
        self.number = number
    pass