# project is a bot that plays simple Ace of Spades, paying out odds worse than true odd of the guess
# players do not pick the card, rather they are betting the next card is the Ace of Spades
# after ace of spades is shown deck should shuffle
# status function should announce how many cards are left in the deck and what the payout odds are

import random


class Card:
    ranks = ['null', 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '{0} of {1}'.format(Card.ranks[self.rank], Card.suits[self.suit]) #returns cards as descriptive strings


class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s += " " * i + str(self.cards[i]) + "\n"
        return s

    def print_deck(self):
        for card in self.cards:
            print(card)

    def shuffle(self):
        num_cards = len(self.cards)
        for i in range(num_cards):
            j = random.randrange(i, num_cards)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def remove(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False

    def pop(self):
        return self.cards.pop()

    def is_empty(self):
        return len(self.cards) == 0

    def deal(self, hands, num_cards=1):
        num_hands = len(hands)
        for i in range(num_cards):
            if self.is_empty(): break  # break if out of cards
            card = self.pop()  # take the "top" card
            hand = hands[i % num_hands]  # whose turn is next?
            hand.add(card)  # add the card to the hand


class Hand(Deck):
    def __init__(self, name=""):
        self.cards = []
        self.name = name

    def add(self, card):
        self.cards.append(card)

deck = Deck()
# deck.shuffle()
# hand = Hand("frank")
# deck.deal([hand], 5)
# print(hand)


class CardGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()


class AceOfSpaces(CardGame):
    def play(self):
        self.hand = ["pile"]
        self.deck.deal(self.hand, 1)
        print(self.hand)

def playGame():
    hand = Hand("pile")
    deck.deal([hand], 1)
    print(hand)

    if hand == Card(3, 13):
        print("It's the", hand, ", you've won!")
        # add code here to pay out
        #deck.shuffle()
        print(deck)

    else:
        print("It's the", hand, ", better luck next time")
        print("There are now", len(deck.cards), "cards remaining, and the new payout is", len(deck.cards)-2, "to 1")


playGame()
print(Card(3,13))
# AceOfSpaces().play()