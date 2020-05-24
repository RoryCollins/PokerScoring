from poker.card import Card


class Hand:
    def __init__(self, string_cards):
        self.cards = [Card(x) for x in string_cards.split(" ")]