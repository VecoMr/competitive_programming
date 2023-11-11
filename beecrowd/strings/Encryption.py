n=int(input())
for _ in range(n):
    s="".join(chr(ord(i)+3) if i.isalpha() else i for i in input())[::-1]
    print(s[:len(s)//2]+"".join(chr(ord(i)-1) for i in s[len(s)//2:]))