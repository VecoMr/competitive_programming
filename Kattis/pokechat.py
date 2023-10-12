s = input()
d = input()
l = [d[i:i+3] for i in range(0,len(d),3)]
print("".join(s[int(i) - 1] for i in l))
