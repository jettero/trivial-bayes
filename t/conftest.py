
import pytest
import nbayes

@pytest.fixture
def trousers():
    data = [['boy', 'trousers']]*6 + [['girl','skirt']]*2 + [['girl','trousers']]*2
    return nbayes.NBayes(*data)

@pytest.fixture
def cards():
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

    return nbayes.NBayes(*[ Card(v+s) for s in 'CDHS' for v in '23456789TJQKA' ])

@pytest.fixture
def email_data():
    return (
        [ 'spam', 'this', 'viagra', 'the-other', 'stuff' ],
        [ 'spam', 'this', 'the-other', 'blah', 'viagra', 'stuff', 'that' ],
        [ 'spam', 'this', 'the-other' ],
        [ 'spam', 'this', 'the-other', 'viagra', 'stuff', 'that' ],
        [ 'spam', 'this', 'the-other', 'blah', 'stuff', 'that' ],
        [ 'spam', 'this', 'the-other', 'blah', 'viagra', 'that' ],
        [ 'spam', 'this', 'the-other', 'blah', 'stuff', 'that' ],
        [ 'spam', 'this', 'the-other', 'blah', 'viagra', 'stuff', 'that' ],
        [ 'spam', 'this', 'blah', 'viagra', 'stuff', 'that' ],
        [ 'spam', 'that', 'viagra' ],
        [ 'spam', 'this', 'the-other', 'blah', 'viagra', 'stuff', 'that' ],
        [ 'spam', 'that', 'this', 'viagra', 'blah' ],
        [ 'spam', 'this', 'blah', 'viagra', 'stuff', 'that' ],
        [ 'spam', 'this', 'the-other', 'that', 'stuff' ],
        [ 'spam', 'this', 'the-other', 'blah', 'viagra', 'that' ],
        [ 'spam', 'this', 'the-other', 'blah', 'viagra', 'that' ],
        [ 'spam', 'viagra', 'blah', 'the-other' ],
        [ 'spam', 'this', 'the-other', 'blah', 'viagra', 'stuff', 'that' ],
        [ 'spam', 'viagra', 'blah', 'the-other', 'stuff' ],
        [ 'spam', 'this', 'viagra', 'blah', 'stuff' ],
        [ 'ham',  'that', 'this', 'blah' ],
        [ 'ham',  'that', 'this', 'blah' ],
        [ 'ham',  'this', 'the-other', 'blah', 'jimmy', 'douglas', 'that' ],
        [ 'ham',  'this', 'the-other', 'blah', 'douglas' ],
        [ 'ham',  'this', 'the-other', 'blah', 'jimmy', 'douglas' ],
        [ 'ham',  'this', 'the-other', 'jimmy', 'douglas', 'that' ],
        [ 'ham',  'this', 'the-other', 'that' ],
        [ 'ham',  'this', 'the-other', 'blah', 'jimmy', 'douglas', 'that' ],
        [ 'ham',  'this', 'the-other', 'blah', 'jimmy', 'douglas', 'that' ],
        [ 'ham',  'the-other', 'blah', 'douglas' ],
        [ 'ham',  'this', 'blah', 'jimmy', 'douglas' ],
        [ 'ham',  'this', 'the-other', 'blah', 'jimmy', 'douglas', 'that' ],
        [ 'ham',  'that', 'this', 'the-other', 'douglas' ],
        [ 'ham',  'this', 'the-other', 'blah', 'jimmy', 'douglas', 'that' ],
        [ 'ham',  'blah', 'jimmy', 'douglas' ],
        [ 'ham',  'this', 'the-other', 'blah', 'jimmy', 'douglas' ],
        [ 'ham',  'this', 'the-other', 'blah', 'jimmy', 'douglas' ],
        [ 'ham',  'the-other', 'blah', 'jimmy', 'douglas', 'that' ],
        [ 'ham',  'this', 'the-other', 'blah', 'douglas', 'that' ],
        [ 'ham',  'this', 'the-other', 'blah', 'jimmy' ],
    )

@pytest.fixture
def emails(email_data):
    return nbayes.Classifier(email_data)

@pytest.fixture
def email_words(email_data):
    wd = {
        'spam': set(),
        'ham':  set(),
        'all':  set(),
    }

    for i in email_data:
        c = i[0]
        w = i[1:]
        wd[c].update(w)

    wd['all']    = wd['spam'].union(wd['ham'])
    wd['spam']  -= wd['ham']
    wd['ham']   -= wd['spam']

    for k in wd:
        wd[k] = list(wd[k])

    return wd
