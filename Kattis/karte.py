s = input()
l = [s[i-3:i] for i in range(3,len(s)+3,3)]
d = {"P": [], "K":[], "H":[], "T":[]}
tm = True
for i in l:
    a,t = i[0], i[1:]
    if t in d[a]:
        tm = False
        break
    else:
        d[a].append(t)
if tm:
    print(*[13-len(d[i]) for i in d])
else:
    print("GRESKA")