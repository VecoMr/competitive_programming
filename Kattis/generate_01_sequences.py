import sys
import random
import subprocess

#####################
#       CONF        #
#####################

MIN = 200
MAX = 200000

av = sys.argv
ac = len(av)

def verif(sequence):
    one = 0
    branch = 1
    inversion = 0
    for bit in sequence:
        if bit == '1':
            one = (one + branch) % 1000000007
        elif bit == '0':
            inversion = (inversion + one) % 1000000007
        else:
            inversion = (2 * inversion + one) % 1000000007
            one = (2 * one + branch) % 1000000007
            branch = 2 * branch % 1000000007
    return inversion

if ac != 2:
    print("USAGE: python3 generate_01_sequences.py NUMBER")
    exit(0)

n = int(av[1])

for i in range(n):
    le = random.randint(MIN, MAX)
    s = ""
    for j in range(le):
        if random.randint(1,500)%150 == 0:
            s+="?"
        else:
            s+= str(random.randint(0,1))
    # execute 0-1sequences.py avec s en stdin
    v = str(verif(s))
    print(v)
    p = subprocess.Popen(["python3", "0-1sequences.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, err = p.communicate(s.encode())
    out = out.decode()
    if err or out != v +"\n":
        print("ERROR")
        break
    print(verif(s))
