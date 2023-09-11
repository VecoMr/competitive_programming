s = input()
while len(s) != 1:
    s = str(eval("*".join(i for i in s if i != "0")))
print(s)