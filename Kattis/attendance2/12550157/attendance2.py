n=int(input())
l=[input() for _ in range(n)]
print("\n".join([l[i] for i in range(0, n) if (i == n - 1 or l[i+1] != "Present!") and l[i] != "Present!"]) or "No Absences")
