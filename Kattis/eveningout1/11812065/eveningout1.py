a, b = map(int,input().split())
print(min(b - a%b, a%b))