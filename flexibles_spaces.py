w, nb_c = map(int,input().split())
c = list(map(int, input().split()))
c.append(0)
c.append(w)
r = []
for i in range(nb_c+1):
    for j in range(i + 1, nb_c+2):
        r.append(abs(c[i]-c[j]))
print(*sorted(set(r)))