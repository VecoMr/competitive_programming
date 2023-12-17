import re

def verif_prime(a):
    if a <= 0:
        return False
    for i in range(2, int(a**0.5) + 1):
        if a%i == 0:
            return False
    return True

l = re.sub("[ ]{2,}", " ", " ".join([i.strip() for i in open(0) if i.strip()])).split(" ")
if sum(1 for i in l if not sum(1 for j in i if j.isdigit())):
    print(0)
else:
    if len(l) != 3:
        print(0)
    else:
        if sum(1 for i in l if i[0] == "0"):
            print(0)
        else:
            a,b,c = map(int, l)
            if verif_prime(b) and verif_prime(c) and b + c == a and a > 3 and a%2 == 0 and a <= 10**9:
                print(1)
            else:
                print(0)
