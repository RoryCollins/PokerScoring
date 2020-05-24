import pytest

from poker import score


@pytest.mark.parametrize("player_one, player_two, winner", [
    ("5D 8C 9S JS AC", "2C 5C 7D 8S QH", "Player 1"),
    ("5H 8C 3S 7S 10D", "3C 6C 7D 5S QH", "Player 2"),
])
def test_highest_number_wins(player_one, player_two, winner):
    assert score(player_one, player_two) == winner


@pytest.mark.parametrize("player_one, player_two, winner", [
    ("5D 5C 9S JS AC", "2C 5C 7D 8S QH", "Player 1"),
    ("5H 5C 3S 7S 10D", "3C 6C 7D 5S QH", "Player 1"),
    ("5H 5C 3S AS 10D", "6C 6H 7D 5S 8H", "Player 2"),
])
def test_pair_wins(player_one, player_two, winner):
    assert score(player_one, player_two) == winner


@pytest.mark.parametrize("player_one, player_two, winner", [
    ("5D 5C 9S 9S AC", "2C 5C 8D 8S QH", "Player 1"),
    ("5H 5C 3S 3H 10D", "3C 6C 7D QS QH", "Player 1"),
    ("5H 5C 3S 3H 10D", "6C 6H 7D 7S 8H", "Player 2"),
    ("5H 5C 3S 3H 10D", "5S 5D 3C 3D 8H", "Player 1"),
])
def test_two_pair_wins(player_one, player_two, winner):
    assert score(player_one, player_two) == winner


@pytest.mark.parametrize("player_one, player_two, winner", [
    ("5H 5C 3S 3H 10D", "6S 6C 6D QS 8H", "Player 2"),
    ("5H 5C 5S 3H 10D", "6S 6C QD QS 8H", "Player 1"),
    ("5H 5C 5S 3H 10D", "6S 6C 6D QS 8H", "Player 2"),
])
def test_three_of_a_kind_wins(player_one, player_two, winner):
    assert score(player_one, player_two) == winner


@pytest.mark.parametrize("player_one, player_two, winner", [
    ("5H 5C 5S 3H 10D", "5S 6C 7D 9S 8H", "Player 2"),
    ("8H 9C 10S JH QD", "5S 6C 7D 9S 8H", "Player 1"),
])
def test_straight_wins(player_one, player_two, winner):
    assert score(player_one, player_two) == winner

