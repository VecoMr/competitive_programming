for j,i in enumerate(open(0)):
    l = list(map(int, i.split()))[1:]
    print(f'Case {j+1}: {min(l)} {max(l)} {max(l)-min(l)}')