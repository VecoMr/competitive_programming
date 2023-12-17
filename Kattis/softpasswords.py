# Read the two password strings
original = input().strip()
attempt = input().strip()

# Check conditions
if original == attempt:
    print("Yes")
elif attempt == original + attempt[-1]:
    print("Yes")
elif attempt[:-1] == original and attempt[-1].isdigit():
    print("Yes")
elif original.swapcase() == attempt:
    print("Yes")
else:
    print("No")
