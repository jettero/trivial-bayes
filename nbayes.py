#!/usr/bin/env python

class instance():
    def __init__(self, label, *attr):
        self.label = label
        self.attr  = attr

class classifier():
    def __init__(self):
        self.corpus = []

    def __str__(self):
        ret = "corpus:\n"
        maxl = 0
        for i in self.corpus:
            if len(i.label) > maxl:
                maxl = len(i.label)
        for i in self.corpus:
            ret += "label: %-*s  attr: %s\n" % (maxl, i.label, i.attr)
        return ret

    def add_instance(self, label='unknown', *attr):
        self.corpus.append( instance(label, *attr) )

    def prob_label(self,label):
        if not self.corpus:
            return 0

        c = 0
        for i in self.corpus:
            if i.label == label:
                c += 1
        return float(c) / len(self.corpus)

    def prob_attr(self,*attr):
        if not self.corpus:
            return 0

        p = []
        for a in attr:
            c = 0
            for i in self.corpus:
                if a in i.attr:
                    c += 1
            p.append( float(c) / len(self.corpus) )
        return reduce(lambda a,b: a*b, p)

    def prob_attr_given_label(self, label, *attr):
        c = 0
        for i in self.corpus:
            if i.label == label:
                if not set(attr) - set(i.attr): 
                    c += 1
        return float(c) / len( self.corpus )

    def prob_label_given_attr(self, label, *attr):
        # P(A|B) = P(B|A)*P(A) / P(B)
        return (self.prob_attr_given_label(label,*attr) * self.prob_label(label)) / self.prob_attr(*attr)
