n,*l=open(0)
t=["keys\n","phone\n","wallet\n"]
for i in l:
    if i in t:
        t.remove(i)
print(*t or ["ready"],sep="")