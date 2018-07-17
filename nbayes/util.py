import math

ONE_LIST_OK = (set,list,tuple,dict)

def _1list(x):
    if not isinstance(x, ONE_LIST_OK):
        return x
    while len(x) == 1 and isinstance(list(x)[0], ONE_LIST_OK):
        x = x[0]
    return iter(x)

def PI(*V):
    r = 1.0
    for v in _1list(V):
        r *= v
    return r

def constrain_probabilities(*P, **kw): # infinitesimal=1e-4):
    infinitesimal = kw.get('infinitesimal', 1e-4)
    # NOTE: This is entirely my own invention for dealing with
    # ZeroDivisionError exceptions. It seems sometimes to be useful anyway
    # though. It may not be a good idea, I'm sure I don't know, but I think it
    # may loosely resemble Laplace Rule of Succession
    #  (n[i]+beta)/(sum([ n[i] ]) + d*beta),
    # which is not a topic I pretend to understand.
    return [ min(1-infinitesimal, max(infinitesimal, float(p))) for p in _1list(P) ]
