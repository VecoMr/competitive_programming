s = list(map(int,input().split("/")))
if s[0] > 12:
    print("EU")
elif s[1] > 12:
    print("US")
else:
    print("either")