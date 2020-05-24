from poker.card import Card


class Hand:
    def __init__(self, cards):
        self.cards = sorted([Card(x) for x in cards], key=lambda x: x.rank)
