from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ObjectProperty, OptionProperty
from kivy.graphics.instructions import *
from Popups import *
from kivy.clock import Clock


from random import randint


from ResizeBehavior import *
from functools import partial
from Square import *
from GamePiece import *
from Board import *
from Player import *
from EventHandler import *
from GameState import *


class StrategoGame(FloatLayout):
    def __init__(self, **kwargs):
        super (StrategoGame, self).__init__()
        #create players
        self.player1 = Player("Red")
        self.player2 = Player("Blue")

        #create aliases for children widgets
        self.board = self.ids["board"]
        self.sidebar = self.ids["sidebar"]

        #gamestatus
        self.activeplayer = self.player1
        self.pieceinhand = None
        self.gamestate = GameState.start_popup

        #set up event handlers for all relevant widgets
        self.eventsobject = EventsMethods(self)
        self.board.eventsobject = self.eventsobject
        self.sidebar.eventsobject = self.eventsobject

        #board also needs to know the active player
        self.board.activeplayer = self.activeplayer

        self.create_start_game_popup()

#gamestate actions

    def change_gamestate(self, newstate):

        #debug
        #print("swap", self.gamestate, "to", newstate)

        self.gamestate = newstate

        if self.gamestate == GameState.player_setup:
            self.player_start()
            self.board.highlight_valid_game_setup_rows()
            self.create_place_pieces_popup()
            self.change_gamestate(GameState.setup_no_piece)

        elif self.gamestate == GameState.setup_no_piece:
            pass

        elif self.gamestate == GameState.pieces_placed:
            for slot in self.sidebar.children:
                slot.disabled = True
            self.change_gamestate(GameState.gameplay_no_piece)
            self.swap_active_player()


        elif self.gamestate == GameState.gameplay_no_piece:
            self.board.clear_all_valid_markers()


        elif self.gamestate == GameState.game_selected_piece:
            self.board.highlight_valid_moves_during_game(self.pieceinhand)

        elif self.gamestate == GameState.conflict:
            self.board.clear_all_valid_markers()




    def swap_active_player(self):
        self.activeplayer.disable_player_pieces()
        if self.activeplayer == self.player1:
            self.activeplayer = self.player2
        else:
            self.activeplayer = self.player1
        #make sure the board knows the new player too...
        self.board.activeplayer = self.activeplayer

        self.activeplayer.activate_player_pieces()

        #debug
        #print("swap activeplayer to " + self.activeplayer.color)



#creating popups
    def create_start_game_popup(self):
        self.startpopup = Popup()
        self.startpopup.center = 670,700
        #apparently the widgets aren't size yet when this is run, need to fix
        #self.center = (self.center_x, self.center_y + self.board.height/2)
        self.startpopup.instructions = "Test your mettle in a game of strategy and cunning!"
        self.startpopup.startbuttontext = "Start a new game!"
        self.startpopup.buttonpress = self.eventsobject.start_game_button_press
        self.add_widget(self.startpopup)


    def create_place_pieces_popup(self):
        self.pp_popup = Popup(title = "Instructions")
        self.pp_popup.center = (self.board.center_x, self.board.center_y + self.board.height/4)
        self.pp_popup.instructions = "The purpose of the game is to capture your opponent's flag.\n" \
                                        "Place your pieces on the highlighted squares in a strategic formation."
        self.pp_popup.startbuttontext = "Got it!"
        self.pp_popup.buttonpress = partial(self.remove_widget, self.pp_popup)

        self.qpp_button = Button(text= "Impatient? Click to randomly place the rest of your pieces.",
                               on_press = self.quick_place_pieces_callback, center = self.pp_popup.center,
                                 size_hint = (None,None), size = (self.pp_popup.width, 100))

        self.add_widget(self.qpp_button)
        self.add_widget(self.pp_popup)

    def quick_place_pieces_callback(self, *args):
        self.quick_place_pieces()
        self.remove_widget(self.qpp_button)



#interacting with the "hand"
    def place_in_hand(self, piece):
        self.pieceinhand = piece


    def clear_hand(self):
        self.pieceinhand = None


#moving pieces around the board

    def update_pieces_left_to_be_placed(self, square):
        if self.pieceinhand.spot.type != "sideboard":
            if square.type == "sideboard":
                self.activeplayer.pieces_left_to_be_placed += 1
            else:
                self.activeplayer.pieces_left_to_be_placed -=1

    def move_to_square(self, square, on_complete=None):
        piece = self.pieceinhand

        #disable inactive pieces so the user can't create unwanted input
        for item in self.activeplayer.pieces:
            item.disabled = True
            #sets the image to the bright one while still disabling the piece
            if item == self.pieceinhand:
                item.state = "down"

        #the most recently added piece is highest on Z axis
        #it's really annoying there's no other way to do this
        self.remove_widget(piece)
        self.add_widget(piece)

        #remove it from the previous spot and put it on new one
        piece.spot.occupied = None

        #piece's animation
        piece.moveanim = Animation(pos = square.pos, t = "out_expo")
        if on_complete:
            piece.moveanim.bind(on_complete = partial(on_complete, self, square))

        piece.moveanim.start(piece)

        #this is necessary since this method is also used before player conflict
        if square.occupied is None:
            self.officially_place_on_square(square, piece)

    def officially_place_on_square(self, square, piece):
        piece.spot = square
        square.occupied = piece
        piece.state = "normal"

        #debug
        #print(piece.id, square.occupied.id)





#creating players & pieces

    def player_start(self):
        '''creates the gamepieces for each player'''

        #initializes the count of how many pieces are left to be placed
        #which will count down to 0
        self.activeplayer.bind(pieces_left_to_be_placed = self.eventsobject.piece_placed)

        for piece, square in zip(self.activeplayer.pieces, self.sidebar.children):
            self.add_widget(piece)
            piece.spot = square
            piece.pos = piece.spot.pos
            piece.size = square.size
            piece.eventsobject = self.eventsobject
            square.occupied = True



#boolean helper functions
    def pieces_are_all_placed(self, *args):
        if self.activeplayer.pieces_left_to_be_placed > 0:
            return False
        #debug
        # print("pieces placed")

        return True

    def piece_belongs_to_activeplayer(self, piece):
        if piece.player_color == self.activeplayer.color:
            return True
        return False


#conflict

    def player_conflict(self, square):
        '''does the conflict animation, moves winner to square and "kills" loser'''
        attacker = self.pieceinhand
        defender = square.occupied

        winner = None
        loser = None

        #special cases first
        if defender.number == 0:
            pass
            #game over, need to write this
        elif (attacker.number == 1 and defender.number == 10) or \
                (attacker.number == 3 and defender.number == 11) or \
                (attacker.number >= defender.number):
            winner = attacker
            loser = defender
        else:
            winner = defender
            loser = attacker

        self.officially_place_on_square(square, winner)

        #makes sure that the pieces are at the top of the Z axis
        self.remove_widget(loser)
        self.remove_widget(winner)
        self.add_widget(loser)
        self.add_widget(winner)

        winner.conflictanim = winner.conflict_animation(winner, 1)
        loser.conflictanim = loser.conflict_animation(loser, -1)
        winner.conflictanim.start(winner)
        loser.conflictanim.start(loser)


    def piece_death(self, instance, piece, *args):
        #debug
        # print(piece.number, "dead")

        #kill the beast! (umm... piece...)
        piece.dead = True

        #find an empty slot on the sidebar.
        #there are not enough slots.... fix this later
        deadslot = None
        for slot in self.sidebar.children:
            if slot.occupied is None:
                deadslot = slot
                break

        piece.disabled = True
        piece.state = "normal"

        #piece's animation
        piece.moveanim = Animation(pos = deadslot.pos, t = "out_expo")
        piece.moveanim.start(piece)

        self.officially_place_on_square(deadslot, piece)




#debug functions

    def quick_place_pieces(self, *args):
        if self.activeplayer.color =="Red":
            x = 6
        else:
            x = 0
        y = 0
        templist = []
        for piece in self.activeplayer.pieces:
            templist.append(piece)
        while len(templist) > 0:
            piece = templist[randint(0,len(templist)-1)]
            self.pieceinhand = piece
            self.move_to_square(self.board.grid[x][y])
            templist.remove(piece)
            self.activeplayer.pieces_left_to_be_placed -= 1
            if y == 9:
                y = 0
                x += 1
            else:
                y += 1


