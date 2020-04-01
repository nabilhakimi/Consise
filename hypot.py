from math import sqrt

def myhypot(x, y):
    return sqrt(x ** 2 + y ** 2)

def main():
    a = float(input("A: "))
    b = float(input("B: "))
    print(f"Hypotenuse: ", myhypot(a, b))
main()
