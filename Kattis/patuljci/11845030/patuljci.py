l = list(map(int,open(0)))

def e(lis, cursor, lis_encours):
    if len(lis_encours) == 7:
        if sum(lis_encours) == 100:
            return lis_encours
        return False
    if cursor > 8:
        return False
    return e(lis, cursor+1, lis_encours) or e(lis, cursor+1, lis_encours + [lis[cursor]])
print(*e(l, 0, []),sep="\n")