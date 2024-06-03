n = int(input())

l = False
s = False

r = ""

alpha = ["clank","bong","click","tap","poing","clonk","clack","ping","tip","cloing","tic","cling","bing","pong","clang","pang","clong","tac","boing","boink","cloink","rattle","clock","toc","clink","tuc"]

for _ in range(n):
    i = input()
    if i == "pop":
        r = r[:-1]
    elif i == "dink":
        s = True
    elif i == "thumb":
        s = False
    elif i == "bump":
        l = not l
    elif i == "whack":
        r += " "
    else:
        if (l and not s) or (s and not l):
            r += chr(ord("A") + alpha.index(i))
        else:
            r += chr(ord("a") + alpha.index(i))
print(r)

    
        
