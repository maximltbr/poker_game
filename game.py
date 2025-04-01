from deck import Deck, Card


class Hand:
    def __init__(self):
        hand = []
        for i in range(5):
            hand.append(deck.deal())
        self._hand = hand

    @property
    def hand(self):
        return self._hand

    def __str__(self):
        return str(self.hand)

    @property
    def is_flush(self):
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
                    continue
                if self.hand[i].rank == self.hand[j].rank:
                    matches += 1
        return matches

    @property
    def is_pair(self):
        if self.num_matches == 2:
            return True
        return False

    @property
    def is_2_pair(self):
        if self.num_matches == 4:
            return True
        return False

    @property
    def is_trips(self):
        if self.num_matches == 6:
            return True
        return False

    @property
    def is_quads(self):
        if self.num_matches == 12:
            return True
        return False

    @property
    def is_full_house(self):
        if self.num_matches == 8:
            return True
        return False

    @property
    def is_straight(self):
        if self.num_matches != 0:
            return False
        self.hand.sort()
        if Card.RANKS.index(self.hand[-1] != Card.RANKS.index(self.hand[0].rank) + 4):
            return False
        return True

# deck = Deck()
# deck.shuffle()
# h = Hand()
# print(h)

matches = 0
count = 0
while matches < 1000:
    deck = Deck()
    deck.shuffle()
    h = Hand()
    count += 1
    if h.is_flush:
        matches += 1
        # break
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
        # break
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
        # break
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
        # break
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
        # break
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
        # break
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
        # break
print(f"The probability of straight is {100*matches/count}%")
