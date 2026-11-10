"""
File: prime_checker.py
Name:Andrew
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""

EXIT = -1


def main():
	"""
	Determine the prime number
	"""
	print("Welcome come to the prime checker")
	while True:
		number = int(input("n:"))
		if number == EXIT:
			print("Have a good one")
			break
		start = 2
		while start != number:
			if 	number % start == 0:
				break
			else:
				start += 1
		if start == number:
			print(str(number) + " is a prime number.")
		else:
			print(str(number) + " is not a prime number.")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
