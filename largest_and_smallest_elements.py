__author__ = 'Taio'

# heapq.nlargest and heapq.nsmallest

import heapq
import random

a = [random.randint(0, 100) for __ in xrange(100)]
print heapq.nsmallest(5, a)
print heapq.nlargest(5, a)
