__author__ = 'Taio'


# collections.defaultdict

import collections

m = dict()
m = collections.defaultdict(int)

print m['a']
print m['b']

m = collections.defaultdict(str)
print m['a']

m['b'] += 'a'
print m['b']

m = collections.defaultdict(lambda: '[default value]')
print m['a']
print m['b']
