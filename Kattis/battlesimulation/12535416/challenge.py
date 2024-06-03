s = input()
l = ["" for _ in s]
s= list(s)
le = len(s)
for i in range(2, le):
    if "".join(sorted(s[i-2:i+1])) == "BLR":
        l[i] = "C"
        s[i-2] = s[i-1] = s[i] = ""

for i in range(le):
    if s[i]:
        l[i] = {"R":"S","B":"K","L":"H"}[s[i]]
print(*l, sep="")