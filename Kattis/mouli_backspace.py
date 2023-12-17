import random
import string

PATH = "test"

l = string.ascii_lowercase

def create_test_file():
    r = ""
    curr = 0
    nb_char = random.randint(100000, 1000000)
    for _ in range(nb_char):
        tmp = 0
        if curr > 0:
            tmp = random.randint(0,1)
        if tmp == 1:
            r+="<"
            curr -= 1
        else:
            r += "".join(random.choices("aze"))
            curr += 1
    # print(1,r,sep="\n")
    with open(PATH, "w") as f:
        f.write("".join(r))