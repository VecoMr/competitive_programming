class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

l = [int(i) for i in open(0)]

root = Node(l.pop(0))

def inserte_node(Root, node):
    if node.val > Root.val:
        if Root.right:
            inserte_node(Root.right, node)
        else:
            Root.right = node
    else:
        if Root.left:
            inserte_node(Root.left, node)
        else:
            Root.left = node

def e(Root):
    if Root.left:
        e(Root.left)
    if Root.right:
        e(Root.right)
    print(Root.val)

while l:
    inserte_node(root, Node(l.pop(0)))

e(root)