from random import uniform
from math import exp


def estimate_area(area, a, b, m, n=1000):
    # Estimate area under x over [a, b] for f positive and <= m.
    hits = 0
    total = m * (b - a)
    for i in range(n):
        x = uniform(a, b)
        y = uniform(0, m)
        if y <= area(x):
            hits += 1
    frac = hits / n
    return frac * total


def area_under_x(x):
    return exp(-x ** 2)


def main():
    print(estimate_area(area_under_x, 0, 2, 1))


main()
