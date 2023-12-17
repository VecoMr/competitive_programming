import random

NB_TEST = 1000
PATH = "test"

with open(PATH, "w") as f:
    for _ in range(NB_TEST):
        f.write(" ".join(str(random.randint(1, 100000)) for _ in range(9)))
        f.write("\n")