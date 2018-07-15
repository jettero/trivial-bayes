# coding: utf-8

def _1list(x):
    if len(x) == 1 and isinstance(x[0], (set,list,tuple,dict)):
        return iter(x[0])
    return iter(x)

class Instance(object):
    def __init__(self, label, *attr):
        self.label = label
        self.attr  = set(_1list(attr))

    def __repr__(self):
        return "nbi({}: {})".format(self.label, self.attr)

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

    def __len__(self):
        return len(self.corpus)

    def add_instances(self, *instances):
        for i in _1list(instances):
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

    def prob_attr(self, attr): # P(B)
        if not self.corpus:
            return 0.0

        c = 0.0
        for i in self.corpus:
            if attr in i.attr:
                c += 1.0
        return c / len(self.corpus)

    def prob_attr_given_label(self, label, attr):  # P(B|A) aka P(attr|label)
        ic = 0
        ac = 0.0
        for i in self.corpus:
            if i.label == label:
                ic += 1
                if attr in i.attr:
                    ac += 1.0
        if ic == 0:
            return 0
        return ac / ic

    def prob_label_given_attr(self, label, attr): # P(A|B) aka P(label|attr)
        p_B = self.prob_attr(attr)                # aka Bayes: P(A|B) = P(B|A)*P(A) / P(B)
        if p_B == 0:
            return 0
        return (self.prob_attr_given_label(label,attr) * self.prob_label(label)) / p_B

    # more generalized P(H|E) = P(E|H)/P(E) * P(H)
    # probability hypothesis is true given evidence
    # is the prior probability P(H) times the likelyhood ratio P(E|H)/P(E)

    def prob_lattr(self,lattr): # P(H) or P(E)
        if not self.corpus:
            return 0.0

        c = 0.0
        for i in self.corpus:
            if lattr in i.lattr:
                c += 1.0
        return c / len(self.corpus)
    prior = prob_lattr

    def prob_lattr_given_lattr(self,e,h): # P(E|H)
        ic = 0
        ac = 0
        for i in self.corpus:
            l = i.lattr
            if h in l:
                ic += 1
                if e in l:
                    ac += 1
        if ic == 0:
            return 0
        return float(ac) / ic

    def likelyhood_ratio(self, e,h): # P(E|H)/P(E)
        return self.prob_lattr_given_lattr(e,h) / self.prob_lattr(e)

    def posterior(self,h,e): # P(E|H)/P(E) * P(H)
        return self.likelyhood_ratio(e,h) * self.prior(h)
