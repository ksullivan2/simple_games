from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from GamePiece import *


class StrategoApp(App):
    def build(self):
        game = GamePiece(1)
        return game

class StrategoGame(GridLayout):
    pass

if __name__ == '__main__':
    StrategoApp().run()
