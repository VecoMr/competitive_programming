n,m=int(input()),int(input())
print(sum([input().count(".")for _ in range(m)])/(n*m))