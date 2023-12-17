def is_factorable(a, b, c):
    return b * b >= 4 * a * c

# Read the number of test cases
num_test_cases = int(input())

# Process each test case
for _ in range(num_test_cases):
    a, b, c = map(int, input().split())
    if is_factorable(a, b, c):
        print("YES")
    else:
        print("NO")