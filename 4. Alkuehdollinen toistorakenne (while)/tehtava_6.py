import math
import random

def likiarvo_laskuri(N,n):
    vastaus = float((n * 4) / N)
    return vastaus

userInput = int(input("pisteiden määrä: "))
N = userInput
n = 0.00

while userInput > 0:
    x = float(random.uniform(-1.00, 1.00) ** 2)
    y = float(random.uniform(-1.00, 1.00) ** 2)

    if x + y < 1:
        n += 1

    userInput -= 1

print(f"Näin monta pistettä jää ympyrän sisälle {n :.0f}")
print(f"Piin likiarvo {likiarvo_laskuri(N, n)}")
