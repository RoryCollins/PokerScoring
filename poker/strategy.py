from abc import ABC, abstractmethod


class Strategy(ABC):
    @staticmethod
    @abstractmethod
    def score(hand):
        pass

    @staticmethod
    def _n_of_a_kind(hand, n):
        ranks = {rank: 0 for rank in [x.rank for x in hand.cards]}
        for card in hand.cards:
            ranks[card.rank] += 1
        for value, freq in ranks.items():
            if freq == n:
                return value
        return 0


class RoyalFlush(Strategy):
    @staticmethod
    def score(hand):
        return 14 if 14 == StraightFlush.score(hand) else 0


class StraightFlush(Strategy):
    @staticmethod
    def score(hand):
        straight_score = Straight.score(hand)
        if straight_score == Flush.score(hand):
            return straight_score
        return 0


class FourOfAKind(Strategy):
    @staticmethod
    def score(hand):
        return Strategy._n_of_a_kind(hand, 4)


class FullHouse(Strategy):
    @staticmethod
    def score(hand):
        ranks = {val: 0 for val in [x.rank for x in hand.cards]}
        for card in hand.cards:
            ranks[card.rank] += 1
        value_set = set(ranks.values())
        if value_set == {2, 3}:
            return max(ranks, key=ranks.get)
        return 0


class Flush(Strategy):
    @staticmethod
    def score(hand):
        handset = set([x.suit for x in hand.cards])
        if len(handset) == 1:
            return max([x.rank for x in hand.cards])
        return 0


class Straight(Strategy):
    @staticmethod
    def score(hand):
        handset = set([x.rank for x in hand.cards])
        if max(handset) - min(handset) + 1 == len(handset) and len(handset) == len(hand.cards):
            return max(handset)
        return 0


class ThreeOfAKind(Strategy):
    @staticmethod
    def score(hand):
        return Strategy._n_of_a_kind(hand, 3)


class TwoPair(Strategy):
    @staticmethod
    def score(hand):
        ranks = {rank: 0 for rank in [x.rank for x in hand.cards]}
        for card in hand.cards:
            ranks[card.rank] += 1
        pairs = [x for x in ranks if ranks[x] == 2]
        if len(pairs) == 2:
            return max(pairs)
        return 0


class Pair(Strategy):
    @staticmethod
    def score(hand):
        return Strategy._n_of_a_kind(hand, 2)


class HighestCard(Strategy):
    @staticmethod
    def score(hand):
        return max(hand.cards, key=lambda card: card.rank).rank
