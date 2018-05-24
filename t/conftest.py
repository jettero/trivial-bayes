
import pytest

@pytest.fixture
def trousers():
    data = [['boy', 'trousers']]*6 + [['girl','skirt']]*2 + [['girl','trousers']]*2
    return nbayes.Classifier(*data)

@pytest.fixture
def deck():
    class Card(nbayes.Instance):
        def __init__(self, card_string):
            labels = set()
            if card_string[0] in 'JQK':
                labels.add('face')
                if card_string[0] == 'K':
                    labels.add('king')
                if card_string[0] == 'J':
                    labels.add('jack')
                if card_string[0] == 'Q':
                    labels.add('queen')
            if card_string[0] == '2':
                labels.add('deuce')
            if card_string[0] == 'A':
                labels.add('ace')
            if card_string[1] in 'CS':
                labels.add('black')
                if card_string[1] == 'C':
                    labels.add('clubs')
                if card_string[1] == 'S':
                    labels.add('spades')
            if card_string[1] in 'DH':
                labels.add('red')
                if card_string[1] == 'D':
                    labels.add('diamonds')
                if card_string[1] == 'H':
                    labels.add('hearts')
            super(Card,self).__init__(card_string, *labels)

    return nbayes.Classifier(*[ Card(v+s) for s in 'CDHS' for v in '23456789TJQKA' ])
