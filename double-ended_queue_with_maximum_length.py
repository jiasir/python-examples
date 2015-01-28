__author__ = 'Taio'


# collections.deque

import collections

last_three = collections.deque(maxlen=3)
for i in xrange(10):
    last_three.append(i)
    print ', '.join(str(x) for x in last_three)
    

