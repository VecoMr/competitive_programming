a,b,c=map(int,input().split())
d,e,f=map(int,input().split())
g=min(a/d, b/e, c/f)
print("%.6f %.6f %.6f" % ((a-g*d),(b-g*e),(c-g*f)))