s = "".join("".join(j for j in i if j in "um") for i in input().split() if not sum(1 for j in i if j != "u" and j != "m" and j.isalpha())).replace("u","1").replace("m","0")
t = ""
r=""
for i in range(0,len(s),7):
    # print(s, s[i:i+7], i)
    r+=chr(int(s[i:i+7],2))
print(r)