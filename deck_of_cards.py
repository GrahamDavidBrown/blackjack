import random

class Card:
    def __init__(self, value, suit, suits=["hearts", "spades", "diamonds", "clubs"]):
        self.value = value
        self.suit = suit
        self.suits = suits


    def short_card(self):
        ret_str = ""
        if self.value == 14 or self.value == 1:
            ret_str += "A"
        elif self.value == 11:
            ret_str += "J"
        elif self.value == 12:
            ret_str += "Q"
        elif self.value == 13:
            ret_str += "K"
        else:
            ret_str += str(self.value)
        ret_str += "o"
        ret_str += self.suit[0].upper()
        return ret_str


    def long_card(self):
        value_translations = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",7: "seven", 8: "eight", 9: "nine",
        10: "ten", 'J': "Jack", "Q": "Queen", "K": "King", "A":"Ace"}
        return "{} of {}".format(value_translations[self.value], self.suit)

    def is_equal(self, other):
        if self.value == other.value and self.suit == other.suit:
            return True
        else:
            return false




class Deck():
    def __init__(self, deck_list):
        self.deck = deck_list
        self.shuffled_deck = []

    def shuffle_deck(self):
        count = 0
        while count < len(self.deck):
            self.shuffled_deck.append((random.choice(self.deck)))
            count += 1
        return self.shuffled_deck
