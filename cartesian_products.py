__author__ = 'Taio'

# itertools.product

import itertools

for p in itertools.product([0, 1], repeat=4):
    print ''.join(str(x) for x in p)