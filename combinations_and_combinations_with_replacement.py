__author__ = 'Taio'


# itertools.combinations and itertools.combinations_with_replacement

import itertools

for c in itertools.combinations([1, 2, 3, 4, 5], 3):
    print ''.join(str(x) for x in c)


for c in itertools.combinations_with_replacement([1, 2, 3], 2):
    print ''.join(str(x) for x in c)
