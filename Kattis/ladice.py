n, l = map(int, input().split())

drawers = [0] * (l + 1)
item_to_drawers = {}
visited = [False] * (n + 1)

def place_item(item, drawer):
    if drawers[drawer] == 0:
        drawers[drawer] = item
        return True
    elif not visited[drawers[drawer]]:
        visited[drawers[drawer]] = True
        other_drawer = item_to_drawers[drawers[drawer]][0] if item_to_drawers[drawers[drawer]][1] == drawer else item_to_drawers[drawers[drawer]][1]
        if place_item(drawers[drawer], other_drawer):
            drawers[drawer] = item
            return True
    return False

for i in range(1, n + 1):
    x, y = map(int, input().split())
    item_to_drawers[i] = [x, y]
    if place_item(i, x) or place_item(i, y):
        print("LADICA")
    else:
        print("SMECE")