#!/usr/bin/env python3

import nbayes
import random
import sys

if len(sys.argv) > 1:
    random.seed( int(sys.argv[1]) )

nwords = ('this', 'that', 'the-other')
swords = ('viagra', 'stuff', 'blah') + nwords
hwords = ('douglas', 'jimmy', 'blah') + nwords
maxwlen = max([ len(x) for x in set(nwords+swords+hwords) ])

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
    def __str__(self):
        return "{}<>".format(self.label)

class Spam(Email):
    src_words = swords

class Ham(Email):
    src_words = hwords

data  = [ Spam().instance for i in range(random.randint(7,20)) ]
data += [  Ham().instance for i in range(random.randint(7,20)) ]

corpus = nbayes.Classifier(data)

print(corpus)
for i in range(len(data)):
    p_spam = corpus.prob_label_not_label_given_attr('spam','ham', data[i].attr)

    ok = result = 'classified correctly'
    if p_spam >= 0.5 and data[i].label == 'ham':
        result = 'false positive'
    if p_spam < 0.5 and data[i].label == 'spam':
        result = 'false negative'

    moar = result
    if result != ok:
        moar += ' ' + str(data[i].attr)
    print("P(spam|data[{:2}]) = {:0.4f} {}".format(i, p_spam, moar))
