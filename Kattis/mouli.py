import random
from mouli_backspace import create_test_file
from subprocess import Popen, PIPE

NB_TEST = 10000
for i in range(NB_TEST):
    create_test_file()
    pytho = Popen(["python3", "backspace.py"], stdin=open("test", "r"), stdout=PIPE)
    cpp = Popen(["./a.out"], stdin=open("test", "r"), stdout=PIPE)
    pytho.wait()
    cpp.wait()
    output_pytho, err_pytho = pytho.communicate()
    output_cpp, err_cpp = cpp.communicate()
    print("Test", i+1, end=": ")
    # print(output_cpp, output_pytho)
    if output_pytho != output_cpp:
        print("Error")
        print("------------- CPP ------------")
        print(output_cpp)
        print("------------ Python -----------")
        print(output_pytho)
        break
    else:
        print("OK")