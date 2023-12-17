s=input()
v="aeiou"
t = 0
r=""

for i in s:
    if t == 0:
        if i in v:
            t = 2
        r += i
    else:
        t -= 1
print(r)