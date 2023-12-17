import random

NB_TEST = 666
PATH = "test"

with open(PATH, "w") as f:
    for _ in range(NB_TEST):
        f.write(f"{random.randint(0,10000)} {random.randint(10,100000)}\n")
    f.write("0 0\n")