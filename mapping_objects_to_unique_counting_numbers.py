__author__ = 'Taio'

# collections.defaultdict

import collections, itertools

value_to_numeric_map = collections.defaultdict(itertools.count().next)

print value_to_numeric_map['a']
print value_to_numeric_map['b']
print value_to_numeric_map['c']
print value_to_numeric_map['a']
print value_to_numeric_map['b']
