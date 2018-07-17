
import pytest
import random

def test_classifier(emails,email_words):
    assert emails.classify( email_words['ham']  ).final == 'ham'
    assert emails.classify( email_words['spam'] ).final == 'spam'
    assert emails.classify( email_words['all']  ).final == None

    emails.default = 'works' # set this initializer -- Classifier(default='works')
    assert emails.classify( email_words['all']  ).final == 'works'

    assert emails.classify( email_words['ham'] + email_words['spam'][0:1]  ).final == 'ham'
    assert emails.classify( email_words['spam'] + email_words['ham'][0:1]  ).final == 'spam'
