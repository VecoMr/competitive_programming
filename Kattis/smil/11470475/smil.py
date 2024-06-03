s = input()
l = len(s)
step = 0
for i in range(l):
    if s[i] in ":;":
        step = 1
    elif step == 1 and s[i] == "-":
        step += 1
    elif step > 0 and s[i] == ")":
        print(i-step)
        step = 0
        
    else:
        step = 0
    