#!/usr/bin/env python

my_iterable = (tuple,list,set,dict)

class Instance(object):
    def __init__(self, label, *attr):
        self.label = label
        self.attr  = set(attr)

    @property
    def lattr(self):
        return set(self.label).union(self.attr)

class Classifier(object):
    def __init__(self, *instances):
        self.corpus = []
        if instances:
            self.add_instances(*instances)

    def __str__(self):
        ret = "corpus:\n"
        maxl = 0
        for i in self.corpus:
            if len(i.label) > maxl:
                maxl = len(i.label)
        for i in self.corpus:
            ret += "  label: {1:{0}}  attr: {2}\n".format(maxl, i.label, i.attr)
        return ret

    def add_instances(self, *instances):
        for i in instances:
            if isinstance(i, Instance):
                self.add_instance(i)
            else:
                self.add_instance(*i)

    def add_instance(self, instance_or_label, *attr):
        if isinstance(instance_or_label, Instance):
            self.corpus.append( instance_or_label )

        else:
            self.corpus.append( Instance(instance_or_label, *attr) )

    def prob_label(self,label): # P(A)
        if not self.corpus:
            return 0.0

        c = 0.0
        for i in self.corpus:
            if i.label == label:
                c += 1.0
        return c / len(self.corpus)

    def prob_attr(self,*attr): # P(B)
        if not self.corpus:
            return 0.0

        c = 0.0
        for i in self.corpus:
            if i.attr.issuperset(attr):
                c += 1.0
        return c / len(self.corpus)

    def prob_attr_given_label(self, label, *attr):  # P(B|A) aka P(attr|label)
        ic = 0
        ac = 0.0
        for i in self.corpus:
            if i.label == label:
                ic += 1
                if i.attr.issuperset(attr):
                    ac += 1.0
        if ic == 0:
            return 0
        return ac / ic

    def prob_label_given_attr(self, label, *attr): # P(A|B) aka P(label|attr)
        p_B = self.prob_attr(*attr)                # aka Bayes: P(A|B) = P(B|A)*P(A) / P(B)
        if p_B == 0:
            return 0
        return (self.prob_attr_given_label(label,*attr) * self.prob_label(label)) / p_B



    # more generalized P(H|E) = P(E|H)/P(E) * P(H)
    # probability hypothesis is true given evidence
    # is the prior probability P(H) times the likelyhood ratio P(E|H)/P(E)

    def prob_lattr(self,*lattr): # P(H) or P(E)
        if not self.corpus:
            return 0.0

        if len(lattr) == 1 and isinstance(lattr[0], my_iterable):
            lattr = lattr[0]

        c = 0.0
        for i in self.corpus:
            if i.lattr.issuperset(lattr) :
                c += 1.0
        return c / len(self.corpus)
    prior = prob_lattr

    def prob_lattr_given_lattr(self,eset,hset): # P(E|H)
        if not isinstance(eset, my_iterable): eset = set([eset])
        if not isinstance(hset, my_iterable): hset = set([hset])
        ic = 0
        ac = 0.0
        for i in self.corpus:
            l = i.lattr
            if l.issuperset(hset):
                ic += 1
                if l.issuperset(eset):
                    ac += 1.0
        if ic == 0:
            return 0
        return ac / ic

    def likelyhood_ratio(self, eset,hset): # P(E|H)/P(E)
        return self.prob_lattr_given_lattr(eset,hset) / self.prob_lattr(eset)

    def posterior(self,hset,eset):
        return self.likelyhood_ratio(eset,hset) * self.prior(hset)
