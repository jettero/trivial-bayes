#!/usr/bin/env python3
# coding: UTF-8

import nbayes

data = [['boy', 'trousers']]*6 + [['girl','skirt']]*2 + [['girl','trousers']]*2

print("""
There is a population of students, 60% boys, 40% girls, all wearing uniforms.
The girls may choose either trousers or skirts (and do so on a 50/50 basis),
but the boys must all wear trousers.

You see a silhouette of a student wearing trousers.  What is the probability
that it is a girl [q1.a]?  A boy [q1.b]?  if you saw the same figure huddled
in the grass nearby (and it was definitely a female student), what would be
the probability she was wearing trousers [q2]?

""")

nbc = nbayes.classifier(*data)
print(nbc)
print("prob girl: {:f} ; prob boy: {:f}"      .format(nbc.prob_label('girl'), nbc.prob_label('boy')))
print("prob trousers given girl: {:f}"        .format(nbc.prob_attr_given_label('girl', 'trousers')))
print("prob trousers given  boy: {:f}"        .format(nbc.prob_attr_given_label('boy',  'trousers')))
print("probability girl given trousers: {:f}" .format(nbc.prob_label_given_attr('girl', 'trousers')))
print("probability boy  given trousers: {:f}" .format(nbc.prob_label_given_attr('boy',  'trousers')))
print("")

print("reverse data")
nbc = nbayes.classifier(*[ a[::-1] for a in data ])
print(nbc)
print("prob trousers: {:f} ; prob skirt: {:f}"  .format(nbc.prob_label('trousers'), nbc.prob_label('skirt')))
print("prob girl given trousers: {:f}"          .format(nbc.prob_attr_given_label('trousers', 'girl')))
print("prob boy  given trousers: {:f}"          .format(nbc.prob_attr_given_label('trousers', 'boy' )))
print("probability trousers given girl: {:f}"   .format(nbc.prob_label_given_attr('trousers', 'girl')))
print("")
