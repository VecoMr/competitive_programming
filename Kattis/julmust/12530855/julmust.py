r = int(input())
i = 1
ans = r//2
print(ans,  flush=True)
right, left = 0, r
s = input()
while s != "exact":
    i += 1
    if s == "less":
        left = ans - 1
    elif s == "more":
        right = ans + 1
    ans = right + (left-right)//2
    print(ans*i, flush=True)
    s = input()