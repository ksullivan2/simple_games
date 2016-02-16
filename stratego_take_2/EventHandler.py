



'''- 1 start:
    newgame: to 0

0 game setup, no piece selected:
    gamepiece press: place in hand, to 1
    all pieces placed: to 2

1 game setup, piece selected
    gamepiece press: remove from hand, to 0
    square press: place pieceinhand on square, to 0

2 all pieces placed:
        #figure out if there's a popup here, wonky now
    gamepiece press: place in hand, to 1
    done button press: if activeplayer is red, to 0, else to 3, switch active player

3 gameplay: no piece selected
    gamepiece press: place in hand, to 4


4 gameplay: piece selected
    gamepiece press: remove from hand, to 3
    opponent piece press: to 5

5 player conflict
    #player conflict actions here
    if not won, to 3
    if won, to 6

6 win popup
    newgame, to 0
    close: close window'''

from kivy.event import EventDispatcher
from kivy.uix.widget import Widget

#-1 is new window
#0 is game setup, no piece selected
#1 is game setup, piece selected
#2 is all pieces placed
#3 is gameplay, no piece selected
#4 is gameplay, piece selected
#5 is player conflict

'''activities associated with leaving the current state
        change the current status to the new status
        activities associated with entering the new state '''


class EventHandlers(EventDispatcher):
    def __init__(self, game):
        self.game = game

    def start_game_button_press(self, *args):
        print("start button press")

        if self.game.gamestate in (-2,2):

            self.game.change_gamestate(-1)

    def gamepiece_press(self, instance):
        if self.game.gamestate == 0:
            self.game.place_in_hand(instance)
            self.game.change_gamestate(1)
        elif self.game.gamestate == 1:
            self.game.clear_hand()
            self.game.change_gamestate(0)
        elif self.game.gamestate == 2:
            pass
        #"are you done" popup
        elif self.game.gamestate == 3:
            self.game.place_in_hand(instance)
            self.game.change_gamestate(4)
        elif self.game.gamestate == 4:
            if self.game.piece_belongs_to_activeplayer(instance):
                self.game.remove_from_hand()
                self.game.change_gamestate(3)
            else:
                self.game.change_gamestate(5)

    def square_press(self,instance):
        #make sure that during state 1, it -=1 to pieces left to be placed
        if self.game.gamestate == 0:
            pass


    def pieces_placed(self):
        if self.game.activeplayer.color == "Red":
            self.game.swap_active_player()
            self.game.change_gamestate(0)
        else:
            self.game.swap_active_player()
            self.game.change_gamestate(1)

