"""
File: complement.py
Name:
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program provides different DNA sequence as
a python string that is case-sensitive.
Your job is to output the complement of them.
"""


def main():
    """
    TODO:
    """
    print(build_complement('ATC'))
    print(build_complement(''))
    print(build_complement('ATGCAT'))
    print(build_complement('GCTATAC'))


def build_complement(dna):
    complement=""
    for i in range(len(dna)):
        if dna[i]=="A":
            complement += "T"
        elif dna[i]=="T":
            complement += "A"
        elif dna[i]=="C":
            complement += "G"
        else:
            complement += "C"
    return complement


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
