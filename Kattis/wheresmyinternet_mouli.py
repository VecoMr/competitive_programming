import random
from subprocess import Popen, PIPE

def create_map():
    n = random.randint(5, 20)
    m = random.randint(n, n + n//2)

    liaison = []
    for i in range(n):
        liaison.append([i+1, random.randint(1, n)])
    for i in range(m-n):
        liaison.append([i+1, random.randint(1, n)])

    # print(n,m)
    # for i in liaison:
    #     print(*i)

    with open("test", "w") as f:
        f.write(str(n))
        f.write(" ")
        f.write(str(m))
        f.write("\n")
        for i in liaison:
            f.write(str(i[0]))
            f.write(" ")
            f.write(str(i[1]))
            f.write("\n")

NB_TEST = 10000
for i in range(NB_TEST):
    create_map()
    pytho = Popen(["python3", "wheresmyinternet.py"], stdin=open("test", "r"), stdout=PIPE)
    cpp = Popen(["./a.out"], stdin=open("test", "r"), stdout=PIPE)
    pytho.wait()
    cpp.wait()
    output_pytho, err_pytho = pytho.communicate()
    output_cpp, err_cpp = cpp.communicate()
    print("Test", i+1, end=": ")
    # print(output_cpp, output_pytho)
    if output_pytho != output_cpp:
        print("Error")
        break
    else:
        print("OK")