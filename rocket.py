"""
File: rocket.py
Name:
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 3 Handout.

"""

# This constant determines rocket size.
SIZE = 5

def head():
    for i in range(SIZE):
        for j in range(SIZE-i):
            print(" ",end="")
        for j in range(i+1):
            print("/",end="")
        for j in range(i + 1):
            print("\\",end="")
        print("")#換行用的

def belt():
    print("+",end="")
    for i in range(SIZE):
        print("=",end="")
        print("=", end="")
    print("+")



def upper_body():
    for i in range(SIZE):
        print("|",end="")
        for j in range(SIZE-i-1):
            print(".",end="")
        for j in range(i+1):
            print("/",end="")
            print("\\",end="")
        for j in range(SIZE-i-1):
            print(".",end="")
        print("|")

def lower_body():
    for i in range(SIZE):
        print("|", end="")
        for j in range(i):
            print(".", end="")
        for j in range(SIZE-i):
            print("\\", end="")
            print("/", end="")
        for j in range(i):
            print(".", end="")
        print("|")



def main():
    head()
    belt()
    upper_body()
    lower_body()
    belt()
    head()

# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
