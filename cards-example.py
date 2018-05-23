#!/usr/bin/env python3

import nbayes
import random

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

c = nbayes.Classifier()
c.add_instances(*[ Card(v+s) for s in 'CDHS' for v in '23456789TJQKA' ])

# prob_lattr is prob label or attr
p_king = c.prob_lattr('king')
p_face = c.prob_lattr('face')
p_face_given_king = c.prob_lattr_given_lattr('face','king')

assert p_king == 4.0/52
assert p_face == 12.0/52
assert p_face_given_king == 1.0 # all kings are faces

p_king_given_face = c.posterior('king','face') # P(H|E) = P(E|H)/P(E) * P(H)
assert p_king_given_face == 1.0/3

print('''
Have someone draw a cards from a deck. They tell you it's a face card, what's
the probability it's a king?

(You could totally do this without invoking Bayes… Here's how you use Bayes.)

''')

print("P(King)              = {:0.4f} aka the prior probability".format(p_king))
print("P(Face)              = {:0.4f} aka the evidence".format(p_face))
print("P(Face|King)         = {:0.4f}".format(p_face_given_king))
print("P(Face|King)/P(Face) = {:0.4f} aka the likelyhood ratio".format(c.likelyhood_ratio('face','king')))
print("P(King|Face)         = P(Face|King)/P(Face) * P(King) aka the posterior probability")
print("                     = {:0.4f}/{:0.4f} * {:0.4f}".format(p_face_given_king, p_face, p_king))
print("                     = {:0.4f}".format( p_king_given_face ))
