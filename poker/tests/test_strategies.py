import pytest

from card import Hand
from strategy import *


@pytest.mark.parametrize("hand, score", [
    ("6D 6S 7H 8S QD", 6),
    ("5D 2S 7H 8S KD", 0)
])
def test_pair(hand, score):
    hand = Hand(hand)
    assert Pair.score(hand) == score


@pytest.mark.parametrize("hand, score", [
    ("5D 6S 7H 8S 9D", 9),
    ("5D 6S 7H 8S 5D", 0)
])
def test_straight(hand, score):
    hand = Hand(hand)
    assert Straight.score(hand) == score


@pytest.mark.parametrize("hand, score", [
    ("4S JS 8S 2S 9S", 11),
    ("5D 6S 7H 8S 5D", 0)
])
def test_flush(hand, score):
    hand = Hand(hand)
    assert Flush.score(hand) == score


@pytest.mark.parametrize("hand, score", [
    ("6D 6S 6H 8S 8D", 6),
    ("5D 6S 7H 8S 5D", 0)
])
def test_full_house(hand, score):
    hand = Hand(hand)
    assert FullHouse.score(hand) == score


@pytest.mark.parametrize("hand, score", [
    ("6D 6S 6H 6C 8D", 6),
    ("5D 6S 7H 5S 5D", 0)
])
def test_four_of_a_kind(hand, score):
    hand = Hand(hand)
    assert FourOfAKind.score(hand) == score


@pytest.mark.parametrize("hand, score", [
    ("6D 6S 6H 6C 8D", 0),
    ("5S 6S 7S 8S 9S", 9),
])
def test_straight_flush(hand, score):
    hand = Hand(hand)
    assert StraightFlush.score(hand) == score


@pytest.mark.parametrize("hand, score", [
    ("6D 6S 6H 6C 8D", 0),
    ("JS AS KS QS 10S", 14),
])
def test_royal_flush(hand, score):
    hand = Hand(hand)
    assert RoyalFlush.score(hand) == score
