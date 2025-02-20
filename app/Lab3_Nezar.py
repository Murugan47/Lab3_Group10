# File: Lab3_Nezar.py
# Author: Nezar Mazraie
# Date: February 19th 2025
# Description: This program calculates the area of Circle, Trapezium, Ellipse, and Rhombus.

import math


def area_circle(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2


def area_trapezium(base1, base2, height):
    if base1 < 0 or base2 < 0 or height < 0:
        raise ValueError("Base and height cannot be negative")
    return 0.5 * (base1 + base2) * height


def area_ellipse(a, b):
    if a < 0 or b < 0:
        raise ValueError("Semi-axes cannot be negative")
    return math.pi * a * b


def area_rhombus(diagonal1, diagonal2):
    if diagonal1 < 0 or diagonal2 < 0:
        raise ValueError("Diagonals cannot be negative")
    return 0.5 * diagonal1 * diagonal2


def main():
    print("Choose a shape to calculate area: Circle, Trapezium, Ellipse, Rhombus")
    shape = input("Enter shape name: ").strip().lower()

    if shape == "circle":
        r = float(input("Enter radius: "))
        print("Area:", area_circle(r))
    elif shape == "trapezium":
        b1 = float(input("Enter base 1: "))
        b2 = float(input("Enter base 2: "))
        h = float(input("Enter height: "))
        print("Area:", area_trapezium(b1, b2, h))
    elif shape == "ellipse":
        a = float(input("Enter semi-axis a: "))
        b = float(input("Enter semi-axis b: "))
        print("Area:", area_ellipse(a, b))
    elif shape == "rhombus":
        d1 = float(input("Enter diagonal 1: "))
        d2 = float(input("Enter diagonal 2: "))
        print("Area:", area_rhombus(d1, d2))
    else:
        print("Invalid shape!")


if __name__ == "__main__":
    main()