from deck import Deck, Card

class Hand:
    """
    Create the Hand class, which will draw 5 cards and store them
    """

    def _init_(self):
        """
        Draw 5 cards from the deck, using a for loop
        """
        hand = []
        for i in range(5):
            hand.append(deck.deal())
        self._hand = hand

    @property
    def hand(self):
        """
        Remove the need for (), saving time.
        returns: the hand
        """
        return self._hand

    def _str_(self):
        return str(self.hand)

    @property
    def is_flush(self):
        """
        Check if the hand is a flush. Established as a property since it is an action.
        """
        for card in self.hand:
            if card.suit != self.hand[0].suit:
                return False
        return True

    @property
    def num_matches(self):
        matches = 0
        for i in range(5):
            for j in range(5):
                if i == j:
                    pass
                elif self.hand[i].rank == self.hand[j].rank:
                    matches += 1
        return matches

    @property
    def is_pair(self):
        if self.num_matches == 2:
            return True
        return False

    @property
    def is_2pair(self):
        if self.num_matches == 4:
            return True
        return False

    @property
    def is_trip(self):
        if self.num_matches == 6:
            return True
        return False

    @property
    def is_quad(self):
        if self.num_matches == 8:
            return True
        return False

    @property
    def is_quad(self):
        if self.num_matches == 12:
            return True
        return False

    @property
    def is_straight(self):
        if self.num_matches != 0:
            return False
        self.cards.sort()
        if Card.RANKS.index(self.cards[-1].rank) != Card.RANKS.index(self.cards[0].rank) + 4:
            return False
        return True

# deck = Deck()
# deck.shuffle()
# h = Hand()
# print(h)

# while True:
#     deck = Deck()
#     deck.shuffle()
#     h = Hand()
#     if h.is_flush:
#         print(h)
#         break

count = 0
matches = 0
while matches < 1000:
    deck = Deck()
    deck.shuffle()
    h = Hand(deck)
    count += 1
    # if h.is_flush:
    #     matches += 1
    if h.is_quad:
        matches += 1
print(100 * (matches / count))