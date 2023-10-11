n = int(input())
t=0
while n:
    if t:
        print()
    t=1
    print(*sorted([input()for _ in "a"*n], key=lambda x: x[:2]), sep="\n")
    n = int(input())
