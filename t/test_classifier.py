
import pytest
import random

def test_classifier(emails,email_words):
    assert emails.classify( email_words['ham']  ).final == 'ham'
    assert emails.classify( email_words['spam'] ).final == 'spam'
    assert emails.classify( email_words['all']  ).final == None

    emails.default = 'works' # set this initializer -- Classifier(default='works')
    assert emails.classify( email_words['all']  ).final == 'works'
