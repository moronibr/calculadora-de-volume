import math

print("Hello")
print("This program reads from the keyboard the three numbers for a tire and computes and outputs the volume of space inside that tire.")

width = input("Enter the width of the tire in mm (ex 205): ")
ratio = input("Enter the aspect ratio of the tire (ex 60): ")
diameter = input("Enter the diameter of the wheel in inches (ex 15): ")

w = float(width)
r = float(ratio)
d = float(diameter)

par = w * r + 2_540 * d

pi = math.pi * w**2 * r * par



calculus = pi / 10_000_000_000

result = "{:.2f}".format(calculus)

print(f" The aproximate volume of space inside the tire is {result} liters.")