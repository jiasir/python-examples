__author__ = 'Taio'

A = {1, 2, 3, 3}
print A

B = {3, 4, 5, 6, 7}
print B

print A | B
print A & B
print A - B
print B - A
print A ^ B
print (A ^ B) == ((A - B) | (B - A))
