from deck_of_cards import *
all_values_list = [2,3,4,5,6,7,8,9,10,11,12,13,14]
all_suits_list = ["hearts", "spades", "diamonds", "clubs"]

class Game:
    def __init__(self, deck, player_hand, dealer_hand, player_bust=False, dealer_bust=False, player_final=0, dealer_final=0):
        self.deck = deck
        self.player_hand = player_hand
        self.dealer_hand = dealer_hand
        self.player_bust = player_bust
        self.dealer_bust = dealer_bust
        self.player_final = 0
        self.dealer_final = 0

    def player_turn(self, deck, hand):
        while 1:
            if self.sum_hand(hand) > 21:
                for item in hand:
                    if item.value == 14:
                        idx = hand.index(item)
                        hand[idx] = (Card(1, item.suit))
                        if self.sum_hand(hand) < 21:
                            break
            for card in hand:
                print(card.short_card(), end=" ")
            print("Your total is: " + str(self.sum_hand(hand)))
            if self.sum_hand(hand) > 21:
                self.player_bust = True
                print("BUST!")
                break
            if self.sum_hand(hand) == 21:
                print("BLACKJACK!")
                break
            else:
                user_in = input("take another hit?(y,n): ").lower()
                if user_in == 'y':
                    hand.append(deck.pop())
                elif user_in == 'n':
                    print("Your final total is: " + str(self.sum_hand(hand)))
                    self.player_final = self.sum_hand(hand)
                    break

    def dealer_turn(self, deck, hand):
        while 1:
            if self.sum_hand(hand) > 21:
                for card in hand:
                    if card.value == 14:
                        idx = hand.index(card)
                        hand[idx] = (Card(1, card.suit))
                        if self.sum_hand(hand) < 21:
                            break
            for card in hand:
                print(card.short_card(), end=" ")
            print("Dealer total is: " + str(self.sum_hand(hand)))
            if self.sum_hand(hand) > 21:
                self.dealer_bust = True
                print("DEALER BUST!")
                break
            if self.sum_hand(hand) == 21:
                print("DEALER BLACKJACK!")
                break
            else:
                if self.sum_hand(hand) <= 17:
                    hand.append(deck.pop())
                else:
                    print("Dealer final total is: " + str(self.sum_hand(hand)))
                    self.dealer_final = self.sum_hand(hand)
                    break

    def sum_hand(self, hand):
        player_total = 0
        for item in hand:
            if item.value == 14:
                player_total -= 3
            elif item.value > 10 and item.value < 14:
                player_total -= (item.value - 10)
            player_total += item.value
        return player_total


deck_list = [Card(val, suit) for suit in all_suits_list for val in all_values_list]
deck = Deck(deck_list)
# for item in deck.deck:
#     print(item.short_card())


def main(deck):
    print("Welome to Blackjack!")
    while 1:
        fresh_deck = deck
        player_hand = []
        player_total = 0
        dealer_hand = []
        dealer_total = 0
        count = 0
        # from line 97 to 118 deck is a list
        deck = deck.shuffle_deck()
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())
        game = Game(deck, player_hand, dealer_hand)
        game.player_turn(deck, game.player_hand)
        game.dealer_turn(deck, game.dealer_hand)
        if game.player_bust and game.dealer_bust:
            print("draw")
        elif game.player_bust and not game.dealer_bust:
            print("player loses")
        elif game.dealer_bust and not game.player_bust:
            print("player wins!")
        elif game.player_final > game.dealer_final:
            print("player wins!")
        elif game.dealer_final > game.player_final:
            print("player loses")
        else:
            print("draw")
        deck = fresh_deck
        game.player_bust = False
        game.dealer_bust = False
        game.player_total = 0
        game.dealer_total = 0
        user_in = input("play again?(y,n): ").lower()
        if user_in == "n":
            break


main(deck)