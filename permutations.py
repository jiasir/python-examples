__author__ = 'Taio'

# itertools.permutations

import itertools

for p in itertools.permutations([1, 2, 3, 4]):
    print ''.join(str(x) for x in p)