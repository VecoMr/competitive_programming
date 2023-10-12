MOD = 1000000007
s = list(input().strip())

def count_ways(s, le):
    r = 0
    for i in range(le-1, -1, -1):
        if s[i] == "1":
            r += le-(i+1)
            le -= 1
    return r

nb = s.count("?")

def generate(s, nb, i, l, le):
    if i >= nb:
        return count_ways(s, le)
    else:
        s[l[i]] = "0"
        r = generate(s, nb, i+1, l, le)
        s[l[i]] = "1"
        r += generate(s, nb, i+1, l, le)
        return r

l=[i for i in range(len(s)) if s[i] == "?"]
le = len(s)
print(generate(s, nb, 0, l, le)%MOD)