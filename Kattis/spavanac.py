h,m = map(int,input().split())
print((h - int(m - 45 < 0)) % 24, (m - 45) % 60)