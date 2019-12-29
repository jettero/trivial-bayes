#!/usr/bin/env python
# coding: utf-8

# I watched 3Blue1Brown's Bayes theorem video:
# https://youtu.be/HZGCoVF3YvM
#
# I wrote this to go along with it:

import nbayes

class Person(nbayes.Instance):
    pass

people = list()

for i in range(10):
    if i<4:
        people.append(Person('librarian', 'meek and tidy'))
    else:
        people.append(Person('librarian'))

for i in range(200):
    if i<20:
        people.append(Person('farmer', 'meek and tidy'))
    else:
        people.append(Person('farmer'))

c = nbayes.Classifier(*people)

print('prior P(H):          {:f}'.format( c.prior('librarian') )) # alias for c.prob_lattr
print('(1/21):              {:f}'.format( 1/21.0 ))
print('likelyhood P(E|H):   {:f}'.format( c.likelyhood('meek and tidy', 'librarian') ))
print('P(¬H) (is farmer):   {:f}'.format( c.prob_lattr('farmer') ))
print('P(¬H) (!librarian):  {:f}'.format( c.prob_lattr('librarian', inverse=True) )) # same
print('P(E|¬H):             {:f}'.format( c.likelyhood('meek and tidy', 'farmer') ))
print('a) P(H)P(E|H):       {:f}'.format( c.prior('librarian') * c.likelyhood('meek and tidy', 'librarian') ))
print('b) P(¬H)P(E|¬H):     {:f}'.format( c.prob_lattr('farmer') * c.likelyhood('meek and tidy', 'farmer') ))
print('a+b:                 {:f}'.format( c.prior('librarian') * c.likelyhood('meek and tidy', 'librarian') +
    c.prob_lattr('farmer') * c.likelyhood('meek and tidy', 'farmer') ))
print('c) P(E):             {:f}'.format( c.prob_lattr('meek and tidy') ))
print('a/c:                 {:f}'.format( c.prior('librarian') * c.likelyhood('meek and tidy', 'librarian') /
    c.prob_lattr('meek and tidy') ))
print('posterior P(H|E):    {:f}'.format( c.posterior('librarian', 'meek and tidy') ))
