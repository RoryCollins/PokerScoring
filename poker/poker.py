from poker.hand import Hand
from poker.strategy import *


def play(line):
    game = line.split(" ")
    hand_one = Hand(game[0:5])
    hand_two = Hand(game[5:10])
    return score(hand_one, hand_two)


def score(hand_one, hand_two):
    strategies = [RoyalFlush, StraightFlush, FourOfAKind, FullHouse, Flush, Straight, ThreeOfAKind, TwoPair, Pair,
                  HighestCard]

    for strategy in strategies:
        player_one_score = strategy.score(hand_one)
        player_two_score = strategy.score(hand_two)
        if player_one_score > player_two_score:
            return 'Player 1'
        elif player_two_score > player_one_score:
            return 'Player 2'
    for card in range(4, 0, -1):
        if hand_one.cards[card].rank > hand_two.cards[card].rank:
            return 'Player 1'
        elif hand_two.cards[card].rank > hand_one.cards[card].rank:
            return 'Player 2'
    return 'Split Pot'
