import pytest

from card import Card


def test_card_translates_regular_card():
    card = Card("6C")
    assert card.suit == "C"
    assert card.rank == 6


@pytest.mark.parametrize("face_card, suit, rank", [
    ("JD", "D", 11),
    ("QS", "S", 12),
    ("KH", "H", 13),
    ("AC", "C", 14),
])
def test_card_translates_face_card(face_card, suit, rank):
    card = Card(face_card)
    assert card.suit == suit
    assert card.rank == rank
