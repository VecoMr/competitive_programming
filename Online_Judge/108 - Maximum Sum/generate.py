import random

NB_TEST = 100
PATH = "test"

with open(PATH, "w") as f:
    for _ in range(NB_TEST):
        n = random.randint(1, 100)
        f.write(f"{str(n)}\n{' '.join(str(random.randint(-127,127)) for i in range(n**2))}\n")