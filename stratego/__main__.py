from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from GamePiece import *
from Terrain import *
from kivy.core.window import Window

Window.size = (700, 700)



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
                if i in (4,5) and j in (2,3,6,7):
                    self.add_widget(Terrain(i,j, land=False))
                else:
                    self.add_widget(Terrain(i,j))







if __name__ == '__main__':
    StrategoApp().run()
