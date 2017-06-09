from math import sqrt
from random import random
import sys

PI = 3.14159
darts = int(sys.argv[1])
circleDarts = 0

for i in range(darts):
    x = random()
    y = random()

    distanceFromOrigin = sqrt(x**2 + y**2)

    if distanceFromOrigin <= 1:     # if it is smaller than the radius, it is in the circle
        circleDarts += 1

print('pi estimate = %.3f' % ((circleDarts/darts) * 4))
