from poker.hand import Hand
from poker.strategy import *


def score(player_one, player_two):
    hand_one = Hand(player_one)
    hand_two = Hand(player_two)
    strategies = [RoyalFlush, StraightFlush, FourOfAKind, FullHouse, Flush, Straight, ThreeOfAKind, TwoPair, Pair,
                  HighestCard]

    for strategy in strategies:
        player_one_score = strategy.score(hand_one)
        player_two_score = strategy.score(hand_two)
        if player_one_score > player_two_score:
            return 'Player 1'
        elif player_two_score > player_one_score:
            return 'Player 2'
    return 'Split Pot'
