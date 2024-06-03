n = int(input())
l = input().split()
print(("makes sense","something is fishy")[sum(1 for i in range(1,n+1) if str(i) != l[i-1] and l[i-1] != "mumble") > 0])