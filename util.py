import math

def _1list(x):
    if len(x) == 1 and isinstance(x[0], (set,list,tuple,dict)):
        return iter(x[0])
    return iter(x)

def PI(*V):
    r = 1.0
    for v in _1list(V):
        r *= v
    return r

def constrain_probabilities(*P, infinitesimal=1e-63):
    return [ min(1-infinitesimal, max(infinitesimal, p)) for p in _1list(P) ]

def underflow_combine_probabilities(*P):
    # this is the straightforward way to compute PI(P)/P(P) + P((1-p)inP)
    # supposedly this can underflow for big lists in P
    P = constrain_probabilities(P)
    p_n = PI(P)
    if p_n == 0.0:
        return 0.0
    p_m = p_n + PI([ 1-p for p in P ])
    return p_n / p_m

def log_dommain_combine_probabilities(*P):
    # same as the underflow_combine_probabilities above, but computed in the log domain
    # https://en.wikipedia.org/w/index.php?title=Naive_Bayes_spam_filtering&oldid=832936482#Other_expression_of_the_formula_for_combining_individual_probabilities
    P = constrain_probabilities(P)
    s = sum([ math.log(1-p) - math.log(p) for p in P ])
    d = math.e ** s + 1.0
    return 1.0 / d

combine_probabilities = underflow_combine_probabilities
