#!/usr/bin/env python
# coding: UTF-8

import nbayes

data = [
  [ 'boy', 'trousers' ],
  [ 'boy', 'trousers' ],
  [ 'boy', 'trousers' ],
  [ 'boy', 'trousers' ],
  [ 'boy', 'trousers' ],
  [ 'boy', 'trousers' ],

  [ 'girl', 'skirt' ],
  [ 'girl', 'skirt' ],
  [ 'girl', 'trousers' ],
  [ 'girl', 'trousers' ],
]

print """
There is a population of students, 60% boys, 40% girls, all wearing uniforms.
The girls may choose either trousers or skirts (and do so on a 50/50 basis),
but the boys must all wear trousers.

You see a silhouette of a student wearing trousers.  What is the probability
that it is a girl [q1.a]?  A boy [q1.b]?  if you saw the same figure huddled
in the grass nearby (and it was definitely a female student), what would be
the probability she was wearing trousers [q2]?

"""

nbc = nbayes.classifier(*data)
print nbc
print "prob girl: %f ; prob boy: %f"        % (nbc.prob_label('girl'), nbc.prob_label('boy'))
print "prob trousers given girl: %f"        % nbc.prob_attr_given_label('girl', 'trousers')
print "prob trousers given  boy: %f"        % nbc.prob_attr_given_label('boy',  'trousers')
print "probability girl given trousers: %f" % nbc.prob_label_given_attr('girl', 'trousers')
print "probability boy  given trousers: %f" % nbc.prob_label_given_attr('boy',  'trousers')
print

atad = map(lambda a: a[::-1], data)
nbc = nbayes.classifier(*atad)
print nbc
print "prob trousers: %f ; prob skirt: %f"  % (nbc.prob_label('trousers'), nbc.prob_label('skirt'))
print "prob girl given trousers: %f"        % nbc.prob_attr_given_label('trousers', 'girl')
print "prob boy  given trousers: %f"        % nbc.prob_attr_given_label('trousers', 'boy' )
print "probability trousers given girl: %f" % nbc.prob_label_given_attr('trousers', 'girl')
print
