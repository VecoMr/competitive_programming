a,b=map(int,input().split())
print(("up","down")[(((b//a)%2)+(b%a>a//2))%2])