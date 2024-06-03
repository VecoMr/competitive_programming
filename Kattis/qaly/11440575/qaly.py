n = int(input())
print(eval("+".join([input().replace(" ", "*") for i in range(n)])))