n = int(input())
l = sum(map(int,input().split()))
print(("yes", "no")[l%3!=0])