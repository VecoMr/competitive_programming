h,w,s = map(int,input().split())
l = sum([input().count(".") for _ in range(h)])
print(f"Your destination will arrive in {l*s+s} meters")