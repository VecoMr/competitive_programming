s = input()
k = s.count("k")
b = s.count("b")
if k < b:
    print("boba")
elif b < k:
    print("kiki")
elif b == k == 0:
    print("none")
else:
    print("boki")
