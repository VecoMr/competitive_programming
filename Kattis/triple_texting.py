s = input()
l = [s[i:i+len(s)//3] for i in range(0,len(s),len(s)//3)]
print((l[0],l[1])[l.count(l[1]) == 2])