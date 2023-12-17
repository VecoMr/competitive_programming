aa1, ab1, aa2, ab2 = map(int,input().split())
ba1, bb1, ba2, bb2 = map(int,input().split())

dist1 = {}
for i in range(aa1, ab1+1):
    for j in range(aa2, ab2+1):
        if (i+j) in dist1:
            dist1[i+j] += 1
        else:
            dist1[i+j] = 1

dist2 = {}
for i in range(ba1, bb1+1):
    for j in range(ba2, bb2+1):
        if (i+j) in dist2:
            dist2[i+j] += 1
        else:
            dist2[i+j] = 1

ld1 = len(dist1)
ld2 = len(dist2)

a1 = sum(i*dist1[i] for i in dist1)/sum(dist1[i] for i in dist1)
a2 = sum(i*dist2[i] for i in dist2)/sum(dist2[i] for i in dist2)

if a1 > a2:
    print("Gunnar")
elif a1 < a2:
    print("Emma")
else:
    print("Tie")

