n = int(input())
for _ in range(n):
    a,b=input(),input()
    print(a,b,"".join(("*",".")[i==j] for i,j in zip(a,b)),sep="\n")