from deck import Deck, Card

class Hand:
    """
    Represents a 5-card poker hand and provides methods to analyze hand types,
    such as flushes, pairs, and other common combinations.
    """
    def __init__(self):
        """Deals a new 5-card hand from a freshly shuffled deck"""
        hand = []
        for i in range(5):
            hand.append(deck.deal())
        self._hand = hand

    @property
    def hand(self):
        """Returns the list of cards in the hand"""
        return self._hand

    def __str__(self):
        """Returns a string representation of the hand"""
        return str(self.hand)

    @property
    def is_flush(self):
        """Returns True if all cards in the hand share the same suit"""
        for card in self.hand:
            if card.suit != self.hand[0].suit:
                return False
        return True

    @property
    def num_matches(self):
        """
        Calculates how many times cards in the hand match by rank
        For instance, a pair will result in 2 matches, three-of-a-kind in 6, etc.
        """
        matches = 0
        for i in range(5):
            for j in range(5):
                if i == j:
                    continue
                if self.hand[i].rank == self.hand[j].rank:
                    matches += 1
        return matches

    @property
    def is_pair(self):
        """Pair: Returns True if the hand contains exactly one pair"""
        return self.num_matches == 2

    @property
    def is_2_pair(self):
        """2 Pair: Returns True if the hand contains two distinct pairs"""
        return self.num_matches == 4

    @property
    def is_trips(self):
        """Trips: Returns True if the hand contains three cards of the same rank"""
        return self.num_matches == 6

    @property
    def is_quads(self):
        """Quads: Returns True if the hand contains four cards of the same rank"""
        return self.num_matches == 12

    @property
    def is_full_house(self):
        """Full House: Returns True if the hand contains a full house (3 of a kind + a pair)"""
        return self.num_matches == 8

    @property
    def is_straight(self):
        """
        Returns True if the hand is a straight (five consecutive ranks).
        Assumes no duplicate ranks.
        """
        if self.num_matches != 0:
            return False
        self.hand.sort()
        if Card.RANKS.index(self.hand[-1]) != Card.RANKS.index(self.hand[0].rank) + 4:
            return False
        return True

# --- Simulations to estimate probabilities of poker hands ---

matches = 0
count = 0
while matches < 1000:
    deck = Deck()
    deck.shuffle()
    h = Hand()
    count += 1
    if h.is_flush:
        matches += 1
print(f"The probability of a flush is {100*matches/count}%")

matches = 0
count = 0
while matches < 1000:
    deck = Deck()
    deck.shuffle()
    h = Hand()
    count += 1
    if h.is_pair:
        matches += 1
print(f"The probability of a pair is {100*matches/count}%")

matches = 0
count = 0
while matches < 1000:
    deck = Deck()
    deck.shuffle()
    h = Hand()
    count += 1
    if h.is_2_pair:
        matches += 1
print(f"The probability of 2 pairs is {100*matches/count}%")

matches = 0
count = 0
while matches < 1000:
    deck = Deck()
    deck.shuffle()
    h = Hand()
    count += 1
    if h.is_trips:
        matches += 1
print(f"The probability of trips is {100*matches/count}%")

matches = 0
count = 0
while matches < 1000:
    deck = Deck()
    deck.shuffle()
    h = Hand()
    count += 1
    if h.is_quads:
        matches += 1
print(f"The probability of quads is {100*matches/count}%")

matches = 0
count = 0
while matches < 100:
    deck = Deck()
    deck.shuffle()
    h = Hand()
    count += 1
    if h.is_full_house:
        matches += 1
print(f"The probability of full house is {100*matches/count}%")

matches = 0
count = 0
while matches < 100:
    deck = Deck()
    deck.shuffle()
    h = Hand()
    count += 1
    if h.is_straight:
        matches += 1
print(f"The probability of straight is {100*matches/count}%")
