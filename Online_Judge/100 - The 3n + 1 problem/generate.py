import random

NB_TEST = 1000
PATH = "test"

with open(PATH, "w") as f:
    for _ in range(NB_TEST):
        a = random.randint(1, 6000)
        b = random.randint(a+1, 10000)
        f.write(f"{a} {b}\n")