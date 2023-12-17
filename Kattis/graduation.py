x, y, nb_c = [int(i) for i in input().split()]
l = list(list(i) for i in zip(*[list(input()) for _ in range(x)]))
def del_letter(l, next, r):
    if not next:
        return
    letter = next.pop(0)
    for i in range(y):
        if letter in l[i]:
            for j in range(x):
                if l[i][j] == letter:
                    l[i][j] = r
                if l[i][j] not in next and l[i][j].isalpha():
                    next.append(l[i][j])
    del_letter(l, next, r)

r = 0
for i in range(y):
    for j in range(x):
        if l[i][j].isalpha():
            r += 1
            del_letter(l, [l[i][j]], str(r))
print(r)
