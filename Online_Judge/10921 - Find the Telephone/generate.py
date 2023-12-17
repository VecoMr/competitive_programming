import string
import random

PATH = "test"
NB_TEST = 420

AVAILABLE = string.ascii_uppercase + "01-"

with open(PATH, "w") as f:
    for _ in range(NB_TEST):
        f.write(f"{''.join(random.choices(AVAILABLE)[0] for _ in range(random.randint(1,30)))}\n")
