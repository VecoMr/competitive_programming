n,m=map(int,input().split())
print(max(eval(input().replace(" ", "*")) for _ in range(n))-m)