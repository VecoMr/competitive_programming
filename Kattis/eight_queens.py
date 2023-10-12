l = [input() for _ in range(8)]
g = []
r = "valid"
for i in l:
    if i.count("*") != 1:
        r = "invalid"
        break
    else:
        g.append(i.index("*"))

if len(g) != len(set(g)):
    r = "invalid"

if r == "valid":
    for i in range(7):
        for j in range(i+1, 8):
            if abs(g[i] - g[j]) == j-i:
                r = "invalid"
                break
        if r == "invalid":
            break
print(r)