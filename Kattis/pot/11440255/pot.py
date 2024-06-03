x = int(input())
l = [input() for i in range(x)]
print(eval("+".join(f'{i[:-1]}**{i[-1]}' for i in l)))