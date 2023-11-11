import random

NB_TEST = 1000
PATH = "TEST"

with open(PATH, "w") as f:
    f.write(str(NB_TEST))
    f.write("\n")
    for _ in range(NB_TEST):
        n = random.randint(1, 100)
        l = [str(random.randint(1, 500)) for _ in range(n)]
        f.write(str(n))
        f.write("\n")
        f.write(" ".join(l))
        f.write("\n")

