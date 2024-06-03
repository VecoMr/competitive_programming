s = input()
print(sum(1 for i in range(len(s)) if s[i]!="PER"[i%3]))