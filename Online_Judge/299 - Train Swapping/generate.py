import random

PATH = "test"
NB_TEST = 1000

with open(PATH, "w") as f:
    f.write(f"{NB_TEST}\n")
    for _ in range(NB_TEST):
        n = random.randint(1,50)
        l = list(range(1,n+1))
        r = []
        for i in range(n):
            r.append(str(l.pop(random.randint(0, n-1-i))))
        f.write(f"{n}\n{' '.join(r)}\n")
