s = input().split()
if len(s) == 1:
    n = int(s[0])
    inst = ""
else:
    n,inst = int(s[0]), s[1]


def nb_nodes(layer):
    return 2**layer

def node_n_depth(size, layer):
    nod = nb_nodes(layer)
    start = sum(nb_nodes(i) for i in range(layer +1, size))
    return [start+1, start+nod]

a = node_n_depth(n+1, len(inst))
le = a[1]-a[0]+1
for i in inst:
    if i == "L":
        a[0] = a[0]+le//2
    elif i == "R":
        a[1] = a[1]-le//2
    le = le//2
print(a[0])