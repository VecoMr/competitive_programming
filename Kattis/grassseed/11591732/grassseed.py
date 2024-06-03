c = float(input())
a = int(input())
l  = [list(map(float, input().split())) for _ in range(a)]
print("%.8f" %sum(eval("*".join([str(i[0]),str(i[1]),str(c)])) for i in l))
