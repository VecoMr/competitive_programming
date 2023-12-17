s = input()

def is_alphabetical(s) -> bool:
    t = list("abcdefghijklmnopqrstuvwxyz")
    for i in s:
        if not t:
            return True
        if i == t[0]:
            t.pop(0)
    print(len(t))
    print(t)
    return not t
is_alphabetical(s)

