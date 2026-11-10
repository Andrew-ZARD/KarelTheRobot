"""
File: hailstone.py
Name:
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    TODO:
    """
    pass
    print("This program computes Hailstone sequences.")
    n = int(input("Please enter a number:"))
    times=0
    """initial time is 0"""
    while n != 1:
        if n%2 == 1:
            n_odd = 3*n+1
            print(str(n)+"is odd number,so I make 3n+1:"+str(n_odd))
            n=n_odd
            times += 1
        else:
            n_even=n//2
            print(str(n)+"is enen number,so I make half:"+str(n_even))
            n=n_even
            times += 1
    print("It took "+str(times)+" steps to reach 1")

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
