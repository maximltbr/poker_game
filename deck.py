import random

class Card:
    RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    SUITS = ["♠️", "♣️", "♦️", "♥️"]

    def _init_(self, rank, suit):
        if rank not in self.RANKS:
            raise ValueError(f"Invalid rank: {rank}")
        if suit not in self.SUITS:
            raise ValueError(f"Invalid suit: {suit}")
        self._rank = rank
        self._suit = suit

    def _str_(self):
        return f"{self.rank}{self.suit}"

    def _repr_(self):
        return self._str_()

    @property
    def rank(self):
        return self._rank

    @property
    def suit(self):
        return self._suit


class Deck:
    def _init_(self):
        _cards = []
        for rank in Card.RANKS:
            for suit in Card.SUITS:
                _cards.append(Card(rank, suit))
        self._deck = _cards

    @property
    def deck(self):
        return self._deck

    def _str_(self):
        return f"{self._deck}"

    def _eq_(self, other):
        return self.rank == other.rank

    def _lt_(self, other):
        return self.RANKS.index(self.rank) < self.RANKS.index(other.rank)

    def shuffle(self):
        random.shuffle(self._deck)

    def deal(self):
        return self._deck.pop(0)


if _name_ == "_main_":
    deck = Deck()
    print(deck)
    deck.shuffle()
    print(deck.deal())

# c1 = Card("A", "♠️")
# print(c1)