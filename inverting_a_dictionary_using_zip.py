__author__ = 'Taio'

m = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print m.items()

print zip(m.values(), m.keys())

mi = dict(zip(m.values(), m.keys()))
print mi