__author__ = 'Taio'

# collections.Counter

import collections

A = collections.Counter([1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 6, 7])
print A
print A.most_common(1)
print A.most_common(3)