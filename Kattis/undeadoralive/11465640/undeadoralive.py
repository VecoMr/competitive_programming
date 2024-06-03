s = input()
a,b = s.count(":)"), s.count(":(")

if a > 0 and b > 0:
    print("double agent")
elif a > 0:
    print("alive")
elif b > 0:
    print("undead")
else:
    print("machine")