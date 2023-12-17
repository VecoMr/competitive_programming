import random

NB_TEST = 666
PATH_TEST = "test"

with open(PATH_TEST, "w") as f:
    for _ in range(NB_TEST):
        f.write(f"{random.randint(10,1000)} {random.randint(10,1000)}\n")