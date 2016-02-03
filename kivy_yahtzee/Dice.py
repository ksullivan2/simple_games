from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.image import Image
from random import randint
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.clock import Clock
from kivy.animation import Animation


class Dice(ToggleButtonBehavior, Image):
        
    def get_image(self, *args):
        '''returns image path for each of the die's sides'''
        if self.state == "down":
            self.source = "images/down_state/dice" + str(self.number) + ".png"
        else:
           self.source  = "images/up_state/dice" + str(self.number) + ".png"

    def roll_animation(self, *args):
        '''returns random dice face, does NOT set the actual number'''
        self.source = "images/up_state/dice" + str(randint(1,6)) + ".png"

    def roll_animation_callback(self, *args):
        '''turns off the dice rolling animation event'''
        Clock.unschedule(self.roll_animation)
        Clock.schedule_once(self.get_image,.1)



class DiceLayer(BoxLayout):
    def __init__(self, **kwargs):
        super(DiceLayer,self).__init__()
        self.hand = []
        for i in range(5):
            self.add_widget(Dice())


    def roll_all_dice(self):
        for dice in self.children:
            if dice.state != "down":
                dice.number = randint(1,6)
                Clock.schedule_interval(dice.roll_animation, .1)
                Clock.schedule_once(dice.roll_animation_callback, .5)


    def pass_values_to_hand(self):
        self.hand = []
        for dice in self.children:
            self.hand.append(dice.number)
        self.hand.sort()
        return self.hand

    def disable_dice(self):
        for dice in self.children:
            dice.disabled = True

    def enable_dice(self):
        for dice in self.children:
            dice.disabled = False
            dice.state = "normal"