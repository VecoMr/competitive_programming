pa, ca, pb, cb, n = map(int, input().split())
l = ()
for i in range(n//ca + 1):
    if (n - i * ca) % cb == 0 :
        if not l or ((n - i * ca)//cb) * pb + (i * pa) < l[0]:
            l = (((n - i * ca)//cb) * pb + (i * pa), i, ((n - i * ca)//cb))
    else:
        if i * ca + ca + (n - i * ca)//cb  > n and (not l or ((n - i * ca)//cb) * pb + (i * pa) + pa < l[0]):
            l = (((n - i * ca)//cb) * pb + (i * pa), i, ((n - i * ca)//cb))
print(l[1], l[2], l[0])