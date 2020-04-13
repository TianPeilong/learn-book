import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, positon):
        return self._cards[positon]

deck = FrenchDeck()

'''
print(len(deck))
print(deck[0])
print(deck[-1])
print(choice(deck))
print(choice(deck))
print(choice(deck))
print(deck[:3])
for card in reversed(deck):
    print(card)
'''

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spaders_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spaders_high):
    print(card)