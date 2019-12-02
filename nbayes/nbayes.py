from .util import _1list
from .instance import Instance

ZERO_COUNT = 0.0

class NBayes(object):
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
            elif isinstance(i, (list,tuple)):
                self.add_instance(*i)
            else:
                raise TypeError("arguments to add_instances() must be lists/tuples or Instances")

    def add_instance(self, instance_or_label, *attr):
        if isinstance(instance_or_label, Instance):
            self.corpus.append( instance_or_label )

        else: # Instance() has internall TypeError checking, no need to check here
            self.corpus.append( Instance(instance_or_label, *attr) )

    def prob_label(self,label): # P(A)
        if not self.corpus:
            return 0.0

        c = ZERO_COUNT
        for i in self.corpus:
            if i.label == label:
                c += 1.0
        return c / len(self.corpus)

    def prob_attr(self, attr): # P(B)
        if not self.corpus:
            return 0.0

        c = ZERO_COUNT
        for i in self.corpus:
            if attr in i.attr:
                c += 1.0
        return c / len(self.corpus)

    def prob_attr_given_label(self, label, attr):  # P(B|A) aka P(attr|label)
        ic = ac = ZERO_COUNT
        for i in self.corpus:
            if i.label == label:
                ic += 1.0
                if attr in i.attr:
                    ac += 1.0
        if ic == 0.0:
            return 0.0
        return ac / ic

    def prob_label_given_attr(self, label, attr): # P(A|B) aka P(label|attr)
        p_B = self.prob_attr(attr)                # aka Bayes: P(A|B) = P(B|A)*P(A) / P(B)
        if p_B == 0:
            return 0
        return (self.prob_attr_given_label(label,attr) * self.prob_label(label)) / p_B

    # more generalized P(H|E) = P(E|H)/P(E) * P(H)
    # probability hypothesis is true given evidence
    # is the prior probability P(H) times the likelyhood ratio P(E|H)/P(E)

    def prob_lattr(self, lattr, inverse=False): # P(H) or P(E)
        if not self.corpus:
            return 0.0

        c = ZERO_COUNT
        for i in self.corpus:
            ilattr = i.lattr
            for l in _iter(lattr):
                if l not in ilattr if inverse else l in ilattr:
                    c += 1.0
        return c / len(self.corpus)
    prior = prob_lattr

    def prob_lattr_given_lattr(self, e,h, inverse=False): # P(E|H)
        ic = ac = ZERO_COUNT
        for i in self.corpus:
            ilattr = i.lattr
            for _h in _iter(h):
                if _h not in ilattr if inverse else _h in ilattr:
                    ic += 1
                    for _e in _iter(e):
                        if _e in ilattr:
                            ac += 1
                            break
        if ic == 0:
            return 0
        return float(ac) / ic

    def likelyhood_ratio(self, e,h, inverse=False): # P(E|H)/P(E)
        b = self.prob_lattr(e, inverse=inverse)
        if b == 0:
            return 0
        return self.prob_lattr_given_lattr(e,h, inverse=inverse) / b

    def posterior(self, h,e, inverse=False): # P(H|E) = P(E|H)/P(E) * P(H)
        return self.likelyhood_ratio(e,h, inverse=inverse) * self.prior(h, inverse=inverse)


def _iter(x):
    if isinstance(x, (dict,list,tuple,set,type(_ for _ in (1,)))):
        yield from x
    else:
        yield x
