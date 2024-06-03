n =int(input())
for j in range(n):
    r, c = map(int, input().split())
    l = [input() for _ in range(r)]
    print(f"Test {j+1}")
    for i in l[::-1]:
        print(i[::-1])
    