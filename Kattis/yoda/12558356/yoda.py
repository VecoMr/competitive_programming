a=input()
b=input()
lm=max(len(a),len(b))
a,b=list(map(int,a.rjust(lm,"0"))),list(map(int,b.rjust(lm,"0")))
c="".join(str(j) for i,j in zip(a,b) if i<=j)
d="".join(str(i) for i,j in zip(a,b) if i>=j)
if d:
    print(int(d))
else:
    print("YODA")
if c:
    print(int(c))
else:
    print("YODA")