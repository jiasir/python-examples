__author__ = 'Taio'


a, b, c = 1, 2, 3
print a, b, c

a, b, c = [1, 2, 3]
print a, b, c

a, b, c = (2 * i + 1 for i in range(3) )
print a, b, c

a, (b, c), d = [1, (2, 3), 4]
print a
print b
print c
print d