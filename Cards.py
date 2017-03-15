#!/usr/bin/python
import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.name_dict = {
            1: "Ace",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Jack",
            12: "Queen",
            13: "King"
        }

    def __str__(self):
        """print out card"""
        return "%s of %s" % (self.name_dict[self.rank], self.suit)


class Deck:
    def __init__(self, shuffle=True):
        self.deck = []
        for rank in range(1,14):
            for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
                self.deck.append(Card(rank, suit))
        if shuffle:
            self.shuffle()

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self, num_cards=1):
        """Deal number of cards into a hand"""
        self.shuffle() # nice shuffling

        cards_in_hand = [self.deck.pop() for i in range(num_cards)]
        return Hand(cards_in_hand)

    def __str__(self):
        """must return a string"""
        return "\n".join([card.__str__() for card in self.deck ])

class Hand:
    def __init__(self, cards=None):
        """define hand class, default empty at runtime"""
        if cards is None:
            self.cards = []
        else:
            self.cards = cards

    def get_hand_total(self):
        """summing up the value of the cards """
        hand_total = 0
        for card in self.cards:
            hand_total += card.rank
        return hand_total

    def __gt__(self, other_hand):
        return self.get_hand_total() > other_hand.get_hand_total()

    def __str__(self):
        return "\n".join([card.__str__() for card in self.cards])


def main():
    """do something"""
    my_deck = Deck()
    print(my_deck)

    # simple implementation of double war game
    my_hand = my_deck.deal(2)
    print("\nYour hand.")
    print(my_hand)

    dealer_hand = my_deck.deal(2)
    print("\nDealer's Hand")
    print(dealer_hand)

    print

    if my_hand > dealer_hand:
        print("You Win.")
    else:
        print("You Lose.")


if __name__ == "__main__":
    main()
