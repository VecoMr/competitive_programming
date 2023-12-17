n = int(input())
for _ in range(n):
    s = input()
    le = int(len(s)**0.5)
    l = list(zip(*[s[i:i+le][::-1] for i in range(0,len(s),le)]))
    print(*["".join(i) for i in l],sep="")
