s = input()
a,s=s[0], s[2:]

def decode(s):
    le = len(s)
    r = ""
    for i in range(0,le,2):
        r += s[i]*int(s[i+1])
    print(r)

def encode(s):
    t = 0
    m = None
    r = ""
    for i in s:
        if i != m:
            if m == None:
                t = 1
                m = i
            else:
                r += f"{m}{t}"
                m = i
                t = 1
        else:
            t += 1
    r += f"{m}{t}"
    print(r)
if a == "D":
    decode(s)
else:
    encode(s)