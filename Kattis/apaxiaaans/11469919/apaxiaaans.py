s=input()
l=len(s)
print(''.join(s[i] for i in range(l) if i == 0 or s[i] != s[i - 1]))