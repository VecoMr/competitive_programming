n = int(input())
la = list(map(int,input().split()))
lb = list(map(int,input().split()))
print(*[i for i in la if i not in lb])