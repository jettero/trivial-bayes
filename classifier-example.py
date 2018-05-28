#!/usr/bin/env python3

import nbayes
import random

nwords = ('this', 'that', 'the-other')
swords = ('viagra', 'stuff', 'blah') + nwords
hwords = ('douglas', 'jimmy', 'blah') + nwords

class Email(object):
    src_words = nwords
    def __init__(self):
        self.words = []
        for i in range(random.randint(5,15)):
            self.words.append( random.choice(self.src_words) )
    @property
    def label(self):
        return self.__class__.__name__.lower()
    @property
    def instance(self):
        return nbayes.Instance(self.label, self.words)

class Spam(Email):
    src_words = swords

class Ham(Email):
    src_words = hwords

data  = [ Spam().instance for i in range(random.randint(7,20)) ]
data += [  Ham().instance for i in range(random.randint(7,20)) ]

corpus = nbayes.Classifier(data)

print(corpus)
p1 = corpus.prob_attr_given_label('spam', 'viagra') * corpus.prob_label('spam')
p2 = corpus.prob_attr_given_label('ham',  'viagra') * corpus.prob_label('ham')
pf = p1 / (p1 + p2)
print("P(spam|viagra) = {}".format(pf))
