input()
print(sum([(int(i)*-1) for i in input().split() if i[0] == '-']))