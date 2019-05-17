from .util import _1list, PI
from .nbayes import NBayes

class Classified(dict):
    class Entry(object):
        def __init__(self, label, p=0, f=0, n=None):
            if not isinstance(label, str):
                raise TypeError("label must be a string")
            try: p = float(p)
            except: raise TypeError("p must be a float (or easily converted to one)")
            try: f = float(f)
            except: raise TypeError("f must be a float (or easily converted to one)")
            try:
                if n is None:
                    n = list()
                n = [ float(i) for i in n ]
            except TypeError:
                raise TypeError('n must be a list of floats (or easily converted to one)')

            self.l = label
            self.p = p # interesting annotation
            self.n = list() if n is None else n # interesting annotation
            self.f = f # final result

        def __repr__(self):
            return "{}<{:f}>({:f}, {})".format(self.l, self.f, self.p, self.n)

    def __init__(self, *a, **kw):
        self.threshold = kw.pop('threshold', 0.1)
        self.default   = kw.pop('default',   None)
        super(Classified, self).__init__(*a, **kw)

    def __repr__(self):
        l = list()
        for k in sorted(self):
            l.append( '{}={:0.4f}'.format(k,self[k].f) )
        return "Classified({}) -> {}".format(', '.join(l), self)

    def __str__(self):
        return str(self.final)

    @property
    def v(self):
        return [ v.f for v in self.values() ]

    @property
    def stat(self):
        ret = dict()
        ret['mean'] = m = sum(self.v) / len(self)
        ret['var']  = v = sum([ (m-v)**2 for v in self.v ])
        ret['ord']  = sorted([ (v.f, v.l) for v in self.values() ], reverse=True)
        return ret

    @property
    def final_mvr(self):
        s = self.stat
        t = [ s['mean'] + (self.threshold + s['var'])*((1+i)/10.0) for i in range(10) ]
        ret = dict()
        for f,l in s['ord']:
            for i,_t in enumerate(t):
                if f >= _t:
                    ret[l] = i
        return ret

    @property
    def final(self):
        s = self.stat
        if len(s['ord']) == 1:
            return s['ord'][0][1]
        if len(s['ord'])>1 and (s['ord'][0][0] - s['ord'][1][0]) >= self.threshold:
            return s['ord'][0][1]
        return self.default

class Classifier(NBayes):
    def __init__(self, *a, **kw):
        self.threshold = kw.pop('threshold', 0.1)
        self.default   = kw.pop('default', None)
        super(Classifier, self).__init__(*a, **kw)

    def classify(self, *attr, **kw): # labels=None, beta=1e-8):
        default   = kw.get('default', self.default)
        threshold = kw.get('threshold', self.threshold)
        beta      = kw.get('beta', 1e-8)
        labels    = kw.get('labels')

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

        res = Classified(default=default, threshold=threshold)
        for label in labels:
            n = [ self.prob_label_given_attr(label,a) for a in _1list(attr) ]
            db = len(n)*beta
            res[label] = Classified.Entry(label, p=sum([ _n+beta for _n in n ])/(len(n)+db), n=n, f=0)
        db = len(res)*beta
        s = sum([ r.p + beta for r in res.values() ]) + db
        for r in res.values():
            r.f = r.p/s
        return res
