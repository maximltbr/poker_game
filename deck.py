import random

class Card:
    """
    Represents a single playing card with a rank (e.g., 'A', '10', 'J') and a suit (e.g., '♣', '♥').
    """
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["♣", "♦", "♥", "♠"]

    def __init__(self, rank, suit):
        """
        Creates a card with the given rank and suit
        Displays an error if either is invalid
        """
        if rank not in self.RANKS:
            raise ValueError("invalid rank")
        if suit not in self.SUITS:
            raise ValueError("invalid suit")
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        """Returns the rank of the card"""
        return self._rank

    @property
    def suit(self):
        """Returns the suit of the card"""
        return self._suit

    def __str__(self):
        """Returns a string version of the card"""
        return f"{self._rank}{self._suit}"

    def __repr__(self):
        """Returns the official string representation of the card"""
        return self.__str__()

    def __eq__(self, other):
        """Checks if two cards have the same rank (ignores suit)"""
        return self.rank == other.rank

    def __lt__(self, other):
        """Compares two cards based on rank order"""
        return self.RANKS.index(self.rank) < self.RANKS.index(other.rank)


class Deck:
    """
    Represents a standard 52-card deck with functionality to shuffle and deal cards
    """
    def __init__(self):
        """Creates a new, ordered deck of 52 cards"""
        _cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                _cards.append(Card(rank, suit))
        self._cards = _cards

    @property
    def cards(self):
        """Returns the list of cards currently in the deck"""
        return self._cards

    def __str__(self):
        """Returns a string showing all the cards in the deck"""
        return str(self._cards)

    def shuffle(self):
        """Shuffles the deck in place"""
        random.shuffle(self.cards)

    def deal(self):
        """Deals (removes and returns) the top card from the deck"""
        return self.cards.pop(0)


if __name__ == "__main__":
    c1 = Card("A", "♣")
    print(c1.suit, c1.rank)
    deck = Deck()
    print(deck)
    deck.shuffle()
    print(deck)
    print(deck.deal())
    print(deck)
