s=list(open(0))
print(" ".join([str(i+1) for i in range(5) if "FBI" in s[i]]) or "HE GOT AWAY!")