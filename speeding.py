n = int(input())
l = [list(map(int,input().split())) for _ in range(n)]
print(max([(l[i+1][1]-l[i][1])//(l[i+1][0]-l[i][0]) for i in range(n-1)]))