__author__ = 'Taio'

# collections.namedtuple
import collections

Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(x=1.0, y=2.0)
print p
print p.x
print p.y