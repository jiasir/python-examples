__author__ = 'Taio'

# collections.Counter

import collections

A = collections.Counter([1, 2, 2])
B = collections.Counter([2, 2, 3])

print A
print B
print A | B
print A & B
print A + B
print A - B
print B - A
