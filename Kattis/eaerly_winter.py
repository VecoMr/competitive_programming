n, t = map(int, input().split())
years = list(map(int, input().split()))
if t < min(years):
    print("It had never snowed this early!")
else:
    print(f"It hadn't snowed this early in {years.index(min(years))} years!")
