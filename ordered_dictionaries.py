__author__ = 'Taio'

# collections.OrderedDict

import collections

m = dict((str(x), x) for x in range(10))
print ', '.join(m.keys())

m = collections.OrderedDict((str(x), x) for x in range(10))
print ', '.join(m.keys())

m = collections.OrderedDict((str(x), x) for x in range(10, 0, -1))
print ', '.join(m.keys())

