n,aze, *l = [(i.strip(), "|")[i.strip() == ""]for i in open(0)]
l = [list(map(int, i.split())) for i in " ".join(l).split("|")]
for i in l:
    a, *b = i
    print(("NO", "YES")[sum(b)%a==0])
