from kivy.app import App
from Dice import *
from yahtzee_definitions import *



class YahtzeeApp(App):
    def build(self):
        return YahtzeeGame()

class YahtzeeGame(BoxLayout):
    pass

   

if __name__ == '__main__':
    YahtzeeApp().run()
