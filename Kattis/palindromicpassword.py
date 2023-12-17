n = int(input())
for _ in range(n):
    s = input()
    le = len(s)
    print(s[:le//2+le%2]+s[:le//2][::-1])