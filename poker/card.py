class Card:
    def __init__(self, representation):
        self.suit = representation[-1]
        self.rank = self.__value(representation[:-1])

    @staticmethod
    def __value(card):
        if card == "T":
            return 10
        if card == "J":
            return 11
        if card == "Q":
            return 12
        if card == "K":
            return 13
        if card == "A":
            return 14
        return int(card)
