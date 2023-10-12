l,r=map(int,input().split())
if l == r == 0 or l < 0 or r < 0:
    print("Not a moose")
elif l == r:
    print("Even", 2*l)
else:
    print("Odd", 2*max(l,r))