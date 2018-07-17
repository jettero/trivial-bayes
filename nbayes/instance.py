
from .util import _1list

class Instance(object):
    def __init__(self, label, *attr):
        self.label = label
        self.attr  = set(_1list(attr))

    def __repr__(self):
        return "nbi({}: {})".format(self.label, self.attr)

    @property
    def lattr(self):
        return set(self.label).union(self.attr)
