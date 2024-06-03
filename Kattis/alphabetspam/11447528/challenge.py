import string

s = input()
l = len(s)
a = (s.count("_")/l)
b = (sum(1 for i in s if i in string.ascii_lowercase)/l)
c = (sum(1 for i in s if i in string.ascii_uppercase)/l)
print(a,b,c,1 - (a+b+c),sep="\n")