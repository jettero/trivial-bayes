
import pytest

def test_cards(cards):
    assert len(cards) == 52
    assert cards.prob_lattr('king') == 4.0/52
    assert cards.prob_lattr('face') == 12.0/52
    assert cards.prob_lattr_given_lattr('face','king') == 1.0
    assert cards.likelyhood_ratio('face','king') == 4 + 1.0/3
    assert cards.posterior('king','face') == 1.0/3
