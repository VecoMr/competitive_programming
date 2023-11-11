import random
s="0123456789"
PATH = "test"
NB_TEST = random.randint(2,5)

with open(PATH, "w") as f:
    f.write(f"{NB_TEST}\n")
    for _ in range(NB_TEST):
        f.write("".join(random.choices(s)[0] for _ in range(random.randint(2,23))))
        f.write("\n")