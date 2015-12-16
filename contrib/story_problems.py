#!/usr/bin/env python
# coding: UTF-8

def Q1():
    P_A1 = 0.4 # probability of a girl, absence of trousers
    P_A2 = 0.6 # probability of a boy, absence of trousers

    P_BgA1 = 0.5 # probability of trousers given that it's a girl
    P_BgA2 = 1.0 # probability of trousers given that it's a boy

    P_A1gB = (P_BgA1*P_A1) / ( (P_BgA1*P_A1) + (P_BgA2*P_A2) )
    print "probability of girl P_A1=%f" % P_A1
    print "probability of boy  P_A2=%f" % P_A2
    print "probability of trousers given girl P_BgA1=%f" % P_BgA1
    print "probability of trousers given boyl P_BgA2=%f" % P_BgA2
    print 
    print "[q1.a] Probability sillouette is a girl given trousers:"
    print "  P_A1gB = (P_BgA1*P_A1) / ( (P_BgA1*P_A1) + (P_BgA2*P_A2) ) = %f" % P_A1gB
    print

    P_A2gB = (P_BgA2*P_A2) / ( (P_BgA1*P_A1) + (P_BgA2*P_A2) )
    print "[q1.b] Probability sillouette is a boy given trousers:"
    print "  P_A2gB = (P_BgA2*P_A2) / ( (P_BgA1*P_A1) + (P_BgA2*P_A2) ) = %f" % P_A2gB
    print

def Q2():
    P_A1 = (0.6*1)+(0.4*0.5) # probability of trousers, absense of gender
    P_A2 = (0.6*0)+(0.4*0.5) # probability of skirts, absense of gender

    P_BgA1 = 0.25 # probability of girl given trousers
    P_BgA2 = 1.00 # probability of girl given skirt

    P_AgB = (P_BgA1 * P_A1)/ ( (P_BgA1*P_A1) + (P_BgA2*P_A2) )
    print "[q2] Probability girl is wearing trousers: %s" % P_AgB


print """
There is a population of students, 60% boys, 40% girls, all wearing uniforms.
The girls may choose either trousers or skirts (and do so on a 50/50 basis),
but the boys must all wear trousers.

You see a silhouette of a student wearing trousers.  What is the probability
that it is a girl [q1.a]?  A boy [q1.b]?  if you saw the same figure huddled
in the grass nearby (and it was definitely a female student), what would be
the probability she was wearing trousers [q2]?

"""

Q1()
Q2()

print """

P(A|B) = P(B|A)*P(A) / P(B)

"""
