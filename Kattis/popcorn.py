# import math
# import numpy as np
# import matplotlib.pyplot as plt

n = int(input())//4
def pop(n):
    q = (n*(n-1))/2
    if n == 0:
        return 0
    else:
        return int(q*4+4)
# l = [pop(i) for i in range(0,10000, 4)]
# print(*l)
# plt.plot(l)
# plt.ylabel('some numbers')
# plt.show()
print(pop(n))