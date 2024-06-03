from decimal import Decimal

a, b, c = map(int, input().split())
print(Decimal(a * b) / Decimal(c))