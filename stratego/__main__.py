from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from GamePiece import *
from Terrain import *


class StrategoApp(App):
    def build(self):
        game = StrategoBoard()
        return game

class StrategoBoard(GridLayout):

    def __init__(self, **kwargs):
        self.board = []
        super(StrategoBoard, self).__init__()
        for i in range(10):
            self.board.append([])
            for j in range(10):
                self.board[i].append(j)
                self.add_widget(Terrain(i,j))






if __name__ == '__main__':
    StrategoApp().run()
