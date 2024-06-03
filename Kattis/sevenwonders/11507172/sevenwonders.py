s=input()
d = {"C":0, "T":0, "G":0}
for i in s:
    d[i] += 1
print(d[min(d, key=lambda x:d[x])]*7 + sum(d[i]**2 for i in d))