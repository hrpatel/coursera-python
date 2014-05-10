# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
DECK = None
player_h = None
dealer_h = None

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []
        self.values = []

    def __str__(self):
        return_val = "Hand contains"
        for card in self.cards:
            return_val = return_val + " " + str(card)
        return return_val

    def add_card(self, card):
        self.cards.append(card)
        self.values.append(VALUES[card.get_rank()])

    def get_value(self):
        # compute the value of the hand
        value = sum(self.values)
        for card_val in self.values:
            if (value + 10) < 22 and card_val == 1:
                value += 10
        return value
   
    def draw(self, canvas, pos):
        pass	# draw a hand on the canvas, use the draw method for cards
 
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.cards = [Card(suit, rank) for suit in SUITS for rank in RANKS]

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.cards)

    def deal_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
    
    def __str__(self):
        return_val = ""
        for card in self.cards:
            return_val = return_val + " " + str(card)
        return return_val


#define event handlers for buttons
def deal():
    global outcome, in_play, DECK, player_h, dealer_h

    # game on!
    in_play = True
    print 
    print "New Game!"
    
    # create and shuffle the deck
    DECK = Deck()
    DECK.shuffle()
    
    # Deal for player
    player_h = Hand()
    player_h.add_card(DECK.deal_card())
    player_h.add_card(DECK.deal_card())
    print "Player: " + str(player_h)
    
    # Deal for dealer
    dealer_h = Hand()
    dealer_h.add_card(DECK.deal_card())
    dealer_h.add_card(DECK.deal_card())
    print "Dealer: " + str(dealer_h)
    

def hit():
    global in_play
    
    # if the hand is in play, hit the player
    if in_play:
        player_h.add_card(DECK.deal_card())
        print "Player hit"
        print str(player_h)
        print "player has: " + str(player_h.get_value())

        # if busted, assign a message to outcome, update in_play and score
        if player_h.get_value() > 21:
            print "Player busted!"
            in_play = False
        
       
def stand():
    global in_play
    
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    while dealer_h.get_value() <= 17: 
        # if busted, assign a message to outcome, update in_play and score
        if player_h.get_value() > 21:
            print "Dealer busted!"
            in_play = False
        else:
            print "dealer has has: " + str(player_h.get_value())

        
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    card = Card("S", "A")
    card.draw(canvas, [300, 300])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()
