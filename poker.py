list_of_suits = {0:"Clubs",1:"Hearts",2:"Diamonds",3:"Spades"}
face_cards = {1:"A",11:"J",12:"Q",13:"K"}
hand_name = {0: "nothing matching",\
                 1: "1 pair",\
                 2: "2 pairs",\
                 3: "3 of a kind",\
                 4: "a straight",\
                 5: "a flush",\
                 6: "a full house",\
                 7: "4 of a kind",\
                 8: "a straight flush",\
                 9: "a royal flush"}

from collections import Counter
import random
import itertools

class Card:
    def __init__(self,suit,number):
        self.suit = suit
        self.number = number
        numname = ""
        if number in face_cards:
            numname = face_cards[number]
        else:
            numname = str(number)
        self.name = (numname + " of " + list_of_suits[suit])



    
class Player:
    def __init__(self,name,money,human=False):
        self.hand = []
        self.money = money
        self.name = name
        self.score = int
        #pass boolean to human, True= human player, False = computer
        self.human = human
        
        #this will track how much $ from the individual is in the pot per round so we can do calls
        self.bet_this_round = 0

        # will set to false when player folds
        self.playing_this_round = True

        #used to compare hands later on
        self.most_common_num = int
        self.most_common_count = int
        self.second_most_common_num = int
        self.second_most_common_count = int

    def check_for_straight(self, numbers):
        for i in range(len(numbers)-1):
            if numbers[i]-numbers[i+1] !=1:
                return False
        return True

    def score_hand(self):
        numbers = []
        suits = []
        for card in self.hand:
            numbers.append(card.number)
            suits.append(card.suit)
        #checks for flush, then if it's Royal, a straight flush, or regular
        if len(set(suits))== 1:
            if numbers == [13,12,11,10,1]:
                self.score = 9
            elif self.check_for_straight(numbers):
                self.score = 8
            else:
                self.score = 5        
        elif self.check_for_straight(numbers):
           self.score = 4
        #finds 2 most common card values, then sees how many and which hand that is 
        cnt = Counter(numbers)
        cnt = cnt.most_common(2)
        if cnt[0][1] == 4:
            self.score = 7
        elif cnt[0][1] == 3:
            if cnt[1][1] == 2:
                self.score = 6
            else:
                self.score = 3
        elif cnt[0][1] == 2:
            if cnt[1][1] == 2:
                self.score = 2
            else:
                self.score = 1
        else:
            self.score = 0

    def sort_hand(self):
        did_something = False
        for index in range(len(self.hand)-1):
            if self.hand[index].number < self.hand[index+1].number:
                self.hand[index], self.hand[index+1] = self.hand[index+1]  , self.hand[index]
                did_something = True
        if did_something == True:
            self.sort_hand()

    def view_hand(player):
        print(player.name + " has " + hand_name[player.score]+ ":")
        for card in player.hand:
            print(card.name)

    
         


#pass this a 2-value list for "valid_range". It's inclusive.
def valid_input(valid_range, message, multiplier=1):
    valid = False
    while valid == False:
        try:
            input_value = int(input(message))
            if input_value in range(valid_range[0],valid_range[1]+1) and input_value%multiplier == 0: 
                valid == True
                break
            elif input_value%multiplier != 0:
                print("Your value must be a multiple of " + str(multiplier))
            else:
                print ("That value is out of range.")
        except (ValueError):
            print ("That was not an integer.")
    return input_value

class Game:
    def __init__(self):
        #arbitrarily limited it to 4 players, $1000 starting money
        #number_of_players = valid_input([1,4],"How many players? ")
        #starting_money = valid_input([50,1000], "How much starting money per player? $50-1000 ")
        #come back later to let them choose starting ante
        self.number_of_players = 4
        #would be nice at some point to choose the number of human players, for now assumes 1 human 3 computer
        starting_money = 100
        self.deck = []
        self.ante = 5
        for suit in range(4):
            for number in range(1,14):
                self.deck.append(Card(suit, number))
        #create all player objects
        #later come back here to ask people to input names
        self.list_of_players = []
        for person in range(0,self.number_of_players):
            name = "Player " + str(person+1)
            self.list_of_players.append(Player(name,starting_money))
        #temporarily forces player 0 to be human
        self.list_of_players[0].human = True
        

    def shuffle_deck(self):
        shuffled_deck = []
        while len(self.deck) > 0:
            random_card_index = random.randint(0,len(self.deck)-1)
            shuffled_deck.append(self.deck[random_card_index])
            del self.deck[random_card_index]
        self.deck = shuffled_deck

    def deal_card(self):
        card = self.deck[0]
        del self.deck[0]
        return card
    

    def new_hand(self):
        self.shuffle_deck()
        cards_left_to_deal = 5
        while cards_left_to_deal >0:
            for person in self.list_of_players:
                person.hand.append(self.deal_card())
            cards_left_to_deal -=1
        for person in self.list_of_players:
            person.sort_hand()
            person.score_hand()

    
        
            

    def get_status(self):
        print()
        for person in self.list_of_players:
            print(person.name)
            print("$" + str(person.money))
            person.view_hand()
            print()
        


def exchange_cards(player):
    player.view_hand()
    indexes_to_exchange = []
    num_cards = valid_input([0,5],"How many cards would you like to exchange? ")
    for card in range(num_cards):
        to_exchange = valid_input([1,5],"One at a time, which card would you like to exchange? (1-5) ")
        while to_exchange in indexes_to_exchange:
            to_exchange = valid_input([1,5],"You've already chosen that card. Which OTHER card? ")
        else:
            indexes_to_exchange.append(to_exchange)
        game.deck.append(player.hand[to_exchange-1])
        player.hand.append(game.deal_card())
    indexes_to_exchange.sort(reverse=True)
    for index in indexes_to_exchange:
        del player.hand[index-1]
    player.sort_hand()
    player.score_hand()
    
        

game = Game()


class Turn:
    def __init__(self):
        self.pot = 0
        self.current_high_bet = 0
        self.won = False
        self.winner = Player
        #does this work? referring to class object?
        #would like to combine last two statements
        
    def print_pot(self):
        print("The pot currently is: $" + str(self.pot))

    def bet(self, player):
        bet = valid_input([5,player.money],"How much would you like to bet/raise? ",5)
        self.add_to_pot(bet, player)
        player.bet_this_round += bet
        if player.bet_this_round > self.current_high_bet:
            self.current_high_bet = player.bet_this_round


    def even_up(self, player):
        difference = self.current_high_bet - player.bet_this_round
        self.pot += difference
        player.money -= difference
        player.bet_this_round = self.current_high_bet
            
    def betting_decisions(self, player):
        print("The current high bet is: $" + str(self.current_high_bet))
        if player.money < (self.current_high_bet - player.bet_this_round):
            valid = False
            while valid == False:
                try:
                    input_value = (input("Go all in? ")).lower()
                    if input_value in ["y", "n", "yes", "no"]: 
                        valid == True
                        break
                except (ValueError):
                    print ("Acceptable responses are 'y, n, yes, no'")
            if input_value in ["y","yes"]:
                bet = self.current_high_bet
                player.money -= bet
                self.pot += bet
                return
            else:
                player.playing_this_round = False
                return
        if self.current_high_bet == 0:
            options = ["knock", "bet", "fold"]
        else:
            options = ["call", "raise", "fold"]

        valid = False
        while valid == False:
            try:
                print("Your options are: " + str(options))
                action = (input("What would you like to do? ")).lower()
                if action in options:
                    valid == True
                    break
                else:
                    print("That was not a valid option.")

            except (ValueError):
                print ("I have no idea why this line is required")
                #keep getting EOF error when this is missing, must investigate further

        if action == "knock":
            return
        elif action == "fold":
            player.playing_this_round = False
            return
        elif action =="call":
            self.even_up(player)
            return
        elif action == "raise":
            self.even_up(player)
            self.bet(player)
            return
        else:
            self.bet(player)
            return
            
            
    def add_to_pot(self, amount, player):
        self.pot += amount
        player.money -=amount

    def win_the_turn(self, player):
        player.money += self.pot
        print(player.name + " has won the pot and now has $" + str(self.winner.money))
            
def make_a_bet(player, turn):
    if player.human == True:
        player.view_hand()
        turn.betting_decisions(player)
        print(player.name + " bet $" + str(player.bet_this_round))
            
    else:
        comp_bet = player.score*5
        bluff = random.randint(0,20)
        #not-really-randomly making the computer bluff
        if bluff == 20:
            comp_bet = comp_bet + 50
        elif bluff > 15:
            comp_bet = comp_bet + 20
        elif bluff > 10:
            comp_bet = comp_bet + 5
        if turn.current_high_bet == 0:
            player.bet_this_round = comp_bet
            turn.current_high_bet = comp_bet
            turn.add_to_pot(comp_bet, player)
            print(player.name + " bet $" + str(player.bet_this_round))
        #if the computer has close to that hand, it'll call
        elif turn.current_high_bet - comp_bet <= 10:
            player.bet_this_round = turn.current_high_bet
            turn.add_to_pot(comp_bet, player)
            print(player.name + " bet $" + str(player.bet_this_round))
        else:
            player.playing_this_round = False
            print(player.name + " has folded.")
            
    
def check_if_one_player_left(turn):
    count = 0
    for player in game.list_of_players:
        if player.playing_this_round == True:
            count +=1
            temp_winner = player        
    if count <=1:
        turn.won = True
        turn.winner = temp_winner
        return True
    return False

def check_if_we_should_continue_betting(turn):
    if check_if_one_player_left(turn) == True:
        return False
    for player in game.list_of_players:
        if player.playing_this_round == True and player.bet_this_round < turn.current_high_bet:
            return True
    return False

def round_of_betting(turn):
    for player in game.list_of_players:
        if player.playing_this_round == True:
            make_a_bet(player, turn)
    while check_if_we_should_continue_betting(turn)==True :
        for player in game.list_of_players:
            if player.playing_this_round == True and player.bet_this_round < turn.current_high_bet:
                make_a_bet(player, turn)

def make_aces_high(player):
    for card in player.hand:
        if card.number == 1:
            card.number = 14
    player.sort_hand()
    
def make_aces_low(player):
    for card in player.hand:
        if card.number == 14:
            card.number = 1
    player.sort_hand()

def two_most_common_values(player, numbers):
    #sorts hand by most common cards
    cnt = Counter(numbers)
    cnt = cnt.most_common(2)

    #counters do not retain the order of the original list, so this makes sure it's in order again
    if cnt[0][1] == cnt[1][1]:
        if cnt[0][0]< cnt[1][0]:
            cnt.insert(0, cnt.pop(1))
    
    #This takes up more memory but I needed a key otherwise so I think this is better
    player.most_common_num = cnt[0][0] 
    player.most_common_count = cnt[0][1]
    player.second_most_common_num = cnt[1][0]
    player.second_most_common_count = cnt[1][1]
    

    
    

    
    

def compare_high_cards(player1, player2):
    #will return the player that won
    
    make_aces_high(player1)
    make_aces_high(player2)

    numbers1 = []
    numbers2 = []

    for index in range(len(player1.hand)):
        numbers1.append(player1.hand[index].number)
        numbers2.append(player2.hand[index].number)
        

    if player1.score in [0, 5]:
        for index in range(len(player1.hand)):
            if player1.hand[index].number > player2.hand[index].number:
                winner = player1
                return winner
            if player1.hand[index].number < player2.hand[index].number:
                winner = player2
                return winner
        if player1.hand[0].suit > player2.hand[0].suit:
            winner = player1
        else:
            winner = player2
        return winner
        
        

    if player1.score in [9,8,4]:
        #if the player has any sort of straight, first it checks if someone has the higher number,
        #then if higher suit
        #damn, i made aces high so now it thinks an A-5 straight beats higher hands (fix later)
        if player1.hand[0].number > player2.hand[0].number:
            winner = player1
        elif player1.hand[0].number < player2.hand[0].number:
            winner = player2
        elif player1.hand[0].suit > player2.hand[0].suit:
            winner = player1
        else:
            winner = player2
        return winner

                         
    two_most_common_values(player1, numbers1)
    two_most_common_values(player2, numbers2)

    #sorts hands by most common number
    for index in range(len(player1.hand)):
        if numbers1[index] == player1.most_common_num:
            numbers1.insert(0, numbers1.pop(index))
        if numbers2[index] == player2.most_common_num:
            numbers2.insert(0, numbers2.pop(index))
    
    if player1.second_most_common_count != 1:
        for index in range(len(player1.hand)):   
            if numbers1[index] == player1.second_most_common_num:
                numbers1.insert(player1.most_common_count, numbers1.pop(index))
            if numbers2[index] == player2.second_most_common_num:
                numbers2.insert(player2.most_common_count, numbers2.pop(index))

    #4 of a kind, 3oaK, and full houses
    #assumes single deck for scope of this program
    if player1.score in [3,6,7]:
        if numbers1[0] > numbers2[0]:
            winner = player1
        else:
            winner = player2
        return winner

    #two pair, one pair
    #very similar to check on straights but I think needs to be different
    #cause i have to sort by most common, not by number value
    if player1.score in [2,1]:
        for index in range(len(numbers1)):
            if numbers1[index] > numbers2[index]:
                winner = player1
                return winner
            if numbers1[index] < numbers2[index]:
                winner = player2
                return winner
        #just in case the hands are identical, it returns the pair with the highest suit
        #looks for person with spades cause we can assume all 4 suits are out
        for card in player1.hand:
            if card.suit == 3 and card.number == cnt1[0][0]:
                winner = player1
                return winner
        winner = player2
    return winner



def turn_in_the_game():
    turn = Turn()
    
    #realizing this is dumb and memory intensive now and I should have just kept turn as part of the Game object
    turn.pot += (game.ante * game.number_of_players)
    turn.print_pot()
    for player in game.list_of_players:
        player.playing_this_round = True
        player.money -= game.ante
    game.new_hand()
    round_of_betting(turn)
    if turn.won == True:
        turn.win_the_turn(turn.winner)
        return
    turn.current_high_bet = 0
    for player in game.list_of_players:
        player.bet_this_round = 0
        if player.playing_this_round == True:
            if player.human ==True:
                exchange_cards(player)
            else:
                pass
                #need to add way for computer to exchange cards!
    print("Let's bet on the new hands.")
    round_of_betting(turn)
    if turn.won == True:
        return
    turn.print_pot()
    high_hand = 0
    for player in game.list_of_players:
        if player.playing_this_round == True:
            if player.score > high_hand or turn.won == False:
                high_hand = player.score
                turn.winner = player
                turn.won = True
            elif turn.won == True and player.score == high_hand:
                turn.winner = compare_high_cards(player, turn.winner)
            
                
    turn.win_the_turn(turn.winner)
    for player in game.list_of_players:
        for number in range(len(player.hand)):
            game.deck.append(player.hand.pop(0))

    game.list_of_players.append(game.list_of_players.pop(0))
    for player in game.list_of_players:
        print(player.name)
       
    
        
    
turn_in_the_game()


 
#computer exchange cards!
#computer bluffing (random)
#compare_high_cards thinks all Aces are high
#should probably switch all the methods that look for hands to have one sort method rather than many
