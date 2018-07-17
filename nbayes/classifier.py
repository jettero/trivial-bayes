
from .util import _1list, PI
from .nbayes import NBayes

class Classified(dict):
    class Entry(object):
        def __init__(self, p=0, f=0, n=None):
            self.p = p # interesting annotation
            self.n = list() if n is None else n # interesting annotation
            self.f = f # final result
        def __repr__(self):
            return "E<{:f}> ({:f}, {})".format(self.f, self.p, self.n)

    def __repr__(self):
        l = list()
        for k in sorted(self):
            l.append( '{}={:0.4f}'.format(k,self[k].f) )
        return "Classified({}) -> {}".format(', '.join(l), self)

    def __str__(self):
        return self.final

    @property
    def final(self):
        m = 0.51
        r = None
        for k in self:
            if self[k].f>m:
                r = k
                m = self[k].f
        return r

class Classifier(NBayes):
    def classify(self, *attr, **kw): # labels=None, beta=1e-8):
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

        res = Classified()
        for label in labels:
            n = [ self.prob_label_given_attr(label,a) for a in _1list(attr) ]
            db = len(n)*beta
            res[label] = Classified.Entry(p=sum([ _n+beta for _n in n ])/(len(n)+db), n=n, f=0)
        db = len(res)*beta
        s = sum([ r.p + beta for r in res.values() ]) + db
        for r in res.values():
            r.f = r.p/s
        return res
