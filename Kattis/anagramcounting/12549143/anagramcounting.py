from collections import Counter
from math import factorial

for i in open(0):
    i = i.strip()
    letter_counts = Counter(i)
    total_anagrams = factorial(len(i))
    for count in letter_counts.values():
        total_anagrams //= factorial(count)
    print(total_anagrams)