def harmonic(n):
    # Compute the sum of 1/k for k = 1 to n.
    total = 0
    for k in range(1, n + 1):
        total += 1 / k
        return total


def main():
    try:
        n = int(input("Enter a positive integer: "))
        print(f"The sum of 1 / k for k = 1 to {n} is {harmonic(n)}")
    except ValueError:  # REDO Exception calls
        print("Please enter a positive integer")
        main()


main()
