
import pytest

def test_trousers(trousers):
    assert len(trousers) == 10
    assert trousers.prob_label('girl') == 0.4
    assert trousers.prob_label('boy') == 0.6
    assert trousers.prob_attr('trousers') == 0.8
    assert trousers.prob_attr_given_label('girl', 'trousers') == 0.5
    assert trousers.prob_attr_given_label('boy', 'trousers') == 1.0
    assert trousers.prob_label_given_attr('girl', 'trousers') == pytest.approx(0.5/0.8 * 0.4)
    assert trousers.prob_label_given_attr('boy', 'trousers') == pytest.approx(1.0/0.8 * 0.6)
