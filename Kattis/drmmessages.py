s = input()
le = len(s)
a, b = s[:le//2], s[le//2:]
sa = sum(ord(i) - ord("A") for i in a)
sb = sum(ord(i) - ord("A") for i in b)
a = [chr((ord(i)-ord("A")+sa)%26+ord("A")) for i in a]
b = [chr((ord(i)-ord("A")+sb)%26+ord("A")) for i in b]
print(*[chr((ord(i)-ord("A")+ord(j)-ord("A"))%26+ord("A")) for i,j in zip(a,b)],sep="")