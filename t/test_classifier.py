
import pytest

def test_classifier(emails,email_data):
    ambig1 = set(['this', 'the-other'])
    ambig2 = set(['this', 'that', 'blah'])
    ambig3 = set(['this', 'that', 'the-other'])

    def _p(x):
        return emails.prob_label_not_label_given_attr('spam','ham', x)

    for ed in email_data:
        a = set(ed[1:])
        p = _p(a)

        if ed[0] == 'spam':
            assert p > 0.5 or a == ambig1
        else:
            assert p < 0.5 or a == ambig2 or a == ambig3

        r = emails.classify(a)
        if p>0.5:
            assert r == 'spam'
        else:
            assert r == 'ham'

        ap = emails.prob_all_labels(a)
        assert ap['spam'] == p

    assert _p(['this'])      == pytest.approx(1.0/2)
    assert _p(['that'])      == pytest.approx(5.0/9)
    assert _p(['the-other']) == pytest.approx(0.48387096774193544)
