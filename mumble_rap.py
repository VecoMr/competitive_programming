input()
print(max(" ".join(i for i in "".join([(" ", j)[j.isdigit()] for j in input()]).split() if i != "").split()))