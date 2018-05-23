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

q1 = nbayes.classifier(*data)

print('Q1', q1)
print("prob girl: {:f} ; prob boy: {:f}"      .format(q1.prob_label('girl'), q1.prob_label('boy')))
print("prob trousers given girl: {:f}"        .format(q1.prob_attr_given_label('girl', 'trousers')))
print("prob trousers given  boy: {:f}"        .format(q1.prob_attr_given_label('boy',  'trousers')))
print("probability girl given trousers: {:f}" .format(q1.prob_label_given_attr('girl', 'trousers')))
print("probability boy  given trousers: {:f}" .format(q1.prob_label_given_attr('boy',  'trousers')))
print("")

q2 = nbayes.classifier(*[ a[::-1] for a in data ])
print('Q2', q2)
print("prob trousers: {:f} ; prob skirt: {:f}"  .format(q2.prob_label('trousers'), q2.prob_label('skirt')))
print("prob girl given trousers: {:f}"          .format(q2.prob_attr_given_label('trousers', 'girl')))
print("prob boy  given trousers: {:f}"          .format(q2.prob_attr_given_label('trousers', 'boy' )))
print("probability trousers given girl: {:f}"   .format(q2.prob_label_given_attr('trousers', 'girl')))
print("")
