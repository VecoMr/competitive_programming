import math
d = {(0, 0.2): 'Logn', (0.3, 1.5): 'Andvari', (1.6, 3.3): 'Kul', (3.4, 5.4): 'Gola', (5.5, 7.9): 'Stinningsgola', (8.0, 10.7): 'Kaldi', (10.8, 13.8): 'Stinningskaldi', (13.9, 17.1): 'Allhvass vindur', (17.2, 20.7): 'Hvassvidri', (20.8, 24.4): 'Stormur', (24.5, 28.4): 'Rok', (28.5, 32.6): 'Ofsavedur', (32.7, math.inf): "Farvidri"}
n = float(input())
for i, j in d:
    if i <= n <= j:
        print(d[(i, j)])