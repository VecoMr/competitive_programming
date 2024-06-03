n=int(input())
a=input()
b=input()
s=True
if n%2:
    for i,j in zip(a,b):
        if i==j:
            s = False
            break
else:
    s = a == b
print(("Deletion failed","Deletion succeeded")[s])