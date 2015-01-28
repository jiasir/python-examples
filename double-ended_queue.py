__author__ = 'Taio'

# collections.deque

import collections

Q = collections.deque()
Q.append(1)
Q.appendleft(2)
Q.extend([3, 4])
Q.extendleft([5, 6])
print Q
print Q.pop()
print Q.popleft()
print Q

Q.rotate(3)
print Q

Q.rotate(-3)
print Q
