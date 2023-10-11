l = [i.strip().split() for i in open(0)]
le = len(l)
for i in range(0, le, 3):
    a,b = map(int, l[i])
    c,d = map(int, l[i+1])
    det = a*d-c*b
    print(f"Case {i//3+1}:")
    print(int(d/det), int(-b/det))
    print(int(-c/det), int(a/det))