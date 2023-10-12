n = int(input())
l = [int(i) for i in input().split()]
print(sum(i for i in l if i!=-1)/sum(1 for i in l if i!=-1))