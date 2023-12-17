n = int(input())
def plank(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return plank(n-1) + plank(n-2) + plank(n-3)
print(plank(n))