n = int(input())
l = [sum(j) for j in list(zip(*[[int(i == "J") for i in input().split()] for _ in range(n)]))]
print(min(l))