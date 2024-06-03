n = int(input())
while (n):
    l = [[]]
    x,y=map(int,input().split())
    m_y = 0
    m_x = 0
    r_y = 0
    while (x > 0 and y > 0):
        if sum(l[-1]) + x > n:
            m_x = max(m_x, sum(l[-1]))
            l.append([x])
            r_y += m_y
            m_y = y
        else:
            l[-1].append(x)
            m_y = max(m_y, y)
        x,y=map(int,input().split())
    m_x = max(m_x, sum(l[-1]))
    r_y+=m_y
    print(f"{m_x} x {r_y}")
    n = int(input())
