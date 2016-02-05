from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from ResizeBehavior import *




from GamePiece import *
from Terrain import *
from StrategoBoard import *



Window.size = (1000, 700)



class StrategoApp(App):
    def build(self):
        game = StrategoWindow()
        return game




if __name__ == '__main__':
    StrategoApp().run()
