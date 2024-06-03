n,m=map(int,input().split())
d={".":20,"O":10,"/":25,"\\":25,"A":35,"^":5,"v":22}
print(sum(sum(d[j]for j in input())for _ in range(n)))