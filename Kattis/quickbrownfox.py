import string
n,*l=open(0)
for i in l:
    s=list(string.ascii_lowercase)
    i=i.lower()
    for j in i:
        if j.isalpha() and j in s:
            s.remove(j)
    if s:
        print("missing",end=" ")
        print(*s,sep="")
    else:
        print("pangram")