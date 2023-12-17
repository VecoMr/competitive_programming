s,n=input().split()
n=int(n)
r = "".join(sorted(list(s)))
le = len(s)
t =le-n*2
if t >= 0:
    if s[n-1:n-1+t] == r[n-1:n-1+t]:
        print("Yes")
    else:
        print("No")
else:
    print("No")