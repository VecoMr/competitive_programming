def is_palindromic_in_base(num, base):
    """Returns True if num is palindromic in the given base, False otherwise."""
    converted = []
    original_num = num
    while num > 0:
        converted.append(num % base)
        num //= base
    # Check if the list of digits is the same when reversed
    return converted == converted[::-1]

def count_palindromic_numbers(l, h, n):
    count = 0
    for num in range(l, h + 1):
        if all(is_palindromic_in_base(num, base) for base in range(2, n + 2)):
            count += 1
    return count

# Read input
l, h, n = map(int, input().split())

# Calculate and print the result
print(count_palindromic_numbers(l, h, n))
