a,b=map(int,input().split())
if a <= b:
    print(f"Dr. Chaz will have {b-a} piece{('','s')[b-a>1]} of chicken left over!")
else:
    print(f"Dr. Chaz needs {a-b} more piece{('','s')[a-b>1]} of chicken!")