from math import pi


def radius():
    try:
        r = int(input("Enter the radius: "))
        area = pi * r ** 2
        print(f"The area of a circle with radius {r} is {area}")
        restart()
    except ValueError:
        print("Please enter radius in numbers only !")
        radius()
    except TypeError:
        print("Invalid Input !")
        restart()


def restart():
    try:
        restart = input("Would you like to calculate another radius?: \n(YES = Y) or (NO = N):")
        if restart.upper() == "Y":
            radius()
        if restart.upper() == "N":
            print("Script terminating. Goodbye.")
    except TypeError:
        print("Invalid Input !")
        restart()


radius()
