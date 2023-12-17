import itertools
import math

a = input()

perms = [int("".join(i)) for i in itertools.permutations(a)]

r = math.inf
a = int(a)
for i in perms:
    if i > a and r > i:
        r = i
if r == math.inf:
    print(0)
else:
    print(r)
        