from random import shuffle
from collections import namedtuple
from itertools import product

Card = namedtuple("Card", "suit value")

class Deck:
    suits = "S H C D".split()
    values = "A 2 3 4 5 6 7 8 9 10 J Q K".split()

    def __init__(self):
        self._cards = [ Card(*card) for card in product(self.suits, self.values) ]

    def __repr__(self):
        return repr(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    def __setitem__(self, pos, item):
        self._cards[pos] = item

    def __len__(self):
        return len(self._cards)

def print_cards(deck):
    for card in deck:
        print(card)
    print()

if __name__ == "__main__":
    deck = Deck()

    print_cards(deck)

    shuffle(deck)

    print_cards(deck)
