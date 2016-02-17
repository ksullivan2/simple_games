from kivy.uix.boxlayout import BoxLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import ObjectProperty
from kivy.animation import Animation
from math import sin, cos
from ResizeBehavior import *


class GamePiece(ToggleButton):
    spot = ObjectProperty(None)

    def __init__(self, number, color, **kwargs):
        self.number = number
        self.player_color = color
        self.dead = False
        self.moveanim = Animation()

        #scouts can move more than 1 space, flags/bombs can't move
        if self.number == 2:
            self.max_spaces = 9
        elif self.number in (0,11):
            self.max_spaces = 0
        else:
            self.max_spaces = 1
        super(GamePiece, self).__init__()

    def get_name(self):
        return names[self.number]

    def conflict_animation(self, instance, direction):
        '''first the pieces circle each other, then "joust" at each other
        direction is 1 for winner, -1 for loser'''

        #circle animation
        radius = 100*direction
        xcenter, ycenter = self.pos

        #current angle IN RADIANS
        #6.28319 radians in 360 degress
        #starts at 90 deg
        angle = 1.57

        #speed IN RADIANS per frame
        speed = .25

        anim = Animation(pos = (xcenter + radius, ycenter), d = .1)

        while angle < 6.28+1.57:
            newx = radius * sin(angle) + xcenter
            newy = radius * cos(angle) + ycenter

            anim += Animation(pos = (newx,newy), d = .03)
            angle += speed

        anim += Animation(pos = (xcenter - radius , ycenter + radius/2), t = "in_out_back")
        anim += Animation(pos = (xcenter + radius , ycenter - radius/2), t = "in_out_back")

        return anim





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

pieceamounts = {0: 1,
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

