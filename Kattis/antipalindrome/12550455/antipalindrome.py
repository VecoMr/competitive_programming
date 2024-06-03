s=[i.lower() for i in input() if i.isalpha()]
def is_pal(a, l=None)->bool:
    if not l: l = len(a)
    for i in range(l//2):
        if a[i] != a[l-1-i]:
            return False
    return True
le = len(s)
for i in range(le):
    for j in range(i+2, le+1):
        if is_pal(s[i:j]):
            print("Palindrome")
            exit(0)
print("Anti-palindrome")