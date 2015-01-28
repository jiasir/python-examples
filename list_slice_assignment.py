__author__ = 'Taio'

a = [1, 2, 3, 4, 5]
a[2:3] = [0, 0]
print a

a[1:1] = [8, 9]
print a

a[1:-1] = []
print a
