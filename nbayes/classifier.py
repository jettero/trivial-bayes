
from .util import _1list, PI
from .instance import Instance

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

    def _classify(self, *attr, **kw): # labels=None, beta=1e-8):
        beta   = kw.get('beta', 1e-8)
        labels = kw.get('labels')
        if labels is None:
            labels = set([ x.label for x in self.corpus ])
        labels = sorted(labels)

        # NOTE: Genest Zidek 1986; cf. Dietrich and List 2014 proposed more or
        # less the below, but with weighted exponents on all p and (1-p) terms
        # ... here, all our weights are 1. It's not clear where the weights
        # would come from anyway. Supervised learning?
        #
        # anyway, this is genestzidek:
        # PI([ p[i]**w[i] ]) / (PI([ p[i]**w[i] ]) + PI([ (1-p[i])**w[i] ])
        # we just set all our weights to 1 (ie, ignore)
        #
        # [ cite https://stats.stackexchange.com/a/188554 ]
        #
        # Thinking the above is the way to go, and finding it doesn't work all
        # that well, I kinda went my own way; though this is also based on the
        # above stackexchange post.
        #
        # p[i] = sum([ n[i]+beta ])/(d + d*beta)
        # f[i] = p[i]/( sum([ p[i] + beta ]) + d*beta )
        #
        # I liked this method because it averages the bayesian outputs p[i] and
        # also puts the other bayesian outputs in an indirect relationship to
        # the one being computed.
        #
        # -Paul

        res = dict()
        for label in labels:
            n = [ self.prob_label_given_attr(label,a) for a in _1list(attr) ]
            db = len(n)*beta
            res[label] = {'p': sum([ n+beta for n in n ])/(len(n)+db), 'n': n}
        db = len(res)*beta
        s = sum([ r['p'] + beta for r in res.values() ]) + db
        for r in res.values():
            r['f'] = r['p']/s
        return res

    def classify(self, *attr, **kw):
        ret = dict()
        res = self._classify(*attr, **kw)
        for label in res:
            ret[label] = res[label]['f']
        return ret
