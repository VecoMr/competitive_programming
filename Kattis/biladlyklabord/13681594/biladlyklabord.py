s=input()
r=s[0]
t=s[0]
for i in s[1:]:
    if i != t:
        t = i
        r+=i
print(r)
