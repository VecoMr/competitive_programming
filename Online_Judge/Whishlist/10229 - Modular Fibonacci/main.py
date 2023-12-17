from typing import *

class Mat:
    def __init__(self, a:int, b:int, c:int, d:int, mod:int) -> None:
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __mul__(self, mat):
        self.a = (self.a * mat.a +self.b * mat.c)
        self.b = (self.a * mat.b +self.b * mat.d)
        self.c = (self.c * mat.a +self.d * mat.c)
        self.d = (self.c * mat.b +self.d * mat.d)

    def __str__(self):
        return f"{self.a} {self.b} {self.c} {self.d}"

for i in open(0):
    n, b = map(int, i.split())
    m = Mat(1, 1, 1, 0, b)
    print(n, b)
    for i in range(n):
        print(m)
        m.__mul__(Mat(1, 1, 1, 0, b))