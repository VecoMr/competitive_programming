l = list(zip(input().split("|"), input().split("|")))
print(*["".join(i) for i in l])