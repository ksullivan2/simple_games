from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.properties import BooleanProperty, ObjectProperty
from ResizeBehavior import *

class Square(Button):
    occupied = ObjectProperty(None, rebind = True, allownone=True)

    def __init__(self, row, col, type):
        self.row = row
        self.col = col
        self.id = str(self.row) + "," + str(self.col)
        self.type = type
        self.valid = False
        super().__init__()

    def get_ids(self):
        return self.id

    def get_background_image(self):
        return "images/" + self.type + ".png"

    def get_disabled_image(self):
        if self.type == "land":
            return "images/land_disabled.png"
        elif self.type == "water":
            return "images/water.png"
        else:
            return "atlas://data/images/defaulttheme/button_disabled"


    def move_to_square(self):
        if self.parent.player.in_hand is not None:
            piece = self.parent.player.in_hand

            #remove it from the previous spot
            piece.spot.occupied = None


            if self.occupied is not None:
                piece = self.player_conflict()

            #set attributes of new spot
            self.occupied = piece
            piece.state = "normal"
            piece.spot = self


    def player_conflict(self):
        attacker = self.parent.player.in_hand
        defender = self.occupied
        winner = None
        loser = None

        #special cases first
        if defender.number == 0:
            pass
            #game over
        elif (attacker.number == 1 and defender.number == 10) or \
                (attacker.number == 3 and defender.number == 11) or \
                (attacker.number >= defender.number):
            winner = attacker
            loser = defender
        else:
            winner = defender
            loser = attacker

        #delete the losing piece, or move it to sidebar??
        #loser.parent.remove_widget(loser)

        print(winner.number)
        return winner








