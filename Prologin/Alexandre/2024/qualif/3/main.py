class City:
    def __init__(self, name, next=None, previous=None) -> None:
        self.name = name
        self.next = next
        self.previous = previous

n = int(input())
m = int(input())

l = [input() for _ in range(n)]
inst = list(input())

incr = 1
curr = None
head = None

for i in l:
    tmp = City(i, next=None, previous=curr)
    if curr:
        curr.next = tmp
    else:
        head = tmp
    curr = tmp

head.previous = curr
curr.next = head
curr = head

queu = []

for i in inst:
    if i == "A":
        if incr == 1:
            curr = curr.next
        else:
            curr = curr.previous
    elif i == "R":
        if incr == 1:
            curr = curr.previous
        else:
            curr = curr.next
        incr = incr *- 1
    elif i == "M":
        queu.append(curr)
        if curr.next is curr:
            curr = None
        else:
            curr.next.previous, curr.previous.next, curr.next, curr.previous, curr = curr.previous, curr.next, None, None, (curr.next, curr.previous)[incr == -1]
    elif i == "C":
        tmp = queu.pop(-1)
        if curr == None:
            curr = tmp
            tmp.next = tmp
            tmp.previous = tmp
        else:
            if incr != 1:
                curr.next.previous, curr.next, tmp.next, tmp.previous = tmp, tmp, curr.next, curr
            else:
                curr.previous.next, curr.previous, tmp.next, tmp.previous = tmp, tmp, curr, curr.previous
            curr = tmp

head = curr

print(curr.name)

if incr == 1:

    curr = curr.next

    while not curr is head:
        print(curr.name)
        curr = curr.next
else:
    curr = curr.previous

    while not curr is head:
        print(curr.name)
        curr = curr.previous

