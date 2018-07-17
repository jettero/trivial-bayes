
def test_classifier(emails):
    assert repr(emails)
    s = str(emails)
    for i in ('label', 'corpus', 'attr'):
        find = i + ':'
        assert find in s
    cr = emails.classify('stringies', default='???')
    assert str(cr)
    assert repr(cr)
    assert str(cr.final) == cr.final
    assert type(cr.final) is str
