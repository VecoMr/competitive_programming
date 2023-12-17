a,b,c=map(int,input().split())
while a or b or c:a,b,c=sorted([a,b,c]);print(("wrong","right")[a**2+b**2==c**2]);a,b,c=map(int,input().split())
