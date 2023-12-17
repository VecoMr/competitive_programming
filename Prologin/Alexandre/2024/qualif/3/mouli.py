from subprocess import Popen, PIPE

nb_test = 1000

for i in range(nb_test):
    with open("test_case", "w") as f:
        create = Popen(["python3", "verif.py"], stdout=f.fileno())
        create.wait(timeout=10)
    with open("test_case", "rb") as f:
        verif = Popen(["./a.out"], stdin=f.fileno(), stdout=PIPE)
        verif.wait(timeout=10)
        verif_out, verif_err = verif.communicate()
        verif_out = verif_out.decode()
    with open("test_case", "rb") as f:
        test = Popen(["python3", "main.py"], stdin=f.fileno(), stdout=PIPE)
        test.wait(timeout=10)
        test_out, test_err = test.communicate()
        test_out = test_out.decode()
    print(i)
    if verif_out != test_out and test_err == None and verif_err == None:
        print("KO :")
        print(f"{verif_out = } {test_out = }")
        break