"""
File: quadratic_solver.py
Name:Andrew
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	TODO:Solving the qudratic equation.
	"""
	a = int(input("Ｃoefficient of quadratic term:"))
	b = int(input("Coefficient of linear term:"))
	c = int(input("Ｃoefficient of quadratic term:"))
	discriminant = b*b-4*a*c
	if discriminant > 0:
		root_1=(-b + math.sqrt(discriminant))/(2*a)
		root_2 = (-b - math.sqrt(discriminant)) / (2 * a)
		print("root_1: "+str(root_1))
		print("root_2: " + str(root_2))
	elif discriminant == 0:
		"""Don't forget that  symbol of equal is == in python."""
		one_root = -b/2*a
		print("One root: "+ str(one_root))
	else:
		print("No real root")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
