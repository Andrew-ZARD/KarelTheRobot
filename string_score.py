"""
File: string_score.py
Name:
------------------------------
This program calculates a score for a given string based on 
the types of characters it contains. It assigns points as follows: 
digits are worth 1 point, uppercase letters are worth 2 points, 
and lowercase letters are worth 3 points. The score() function 
goes through each character in the string, adds up the points 
according to its type, and then prints out the total score.
"""


def main():
    """
    TODO:
    """
    score('1aB4rC')    # digit->1 ; upper->2; lower->3
    # 12
    score('aaaaA3')
    # 15


def score(string):
    count=0
    for i in range(len(string)):
        if string[i].isdigit():
            count += 1
        elif string[i].islower():
            count += 3
        else:
            count += 2
    ans= print(str(count))
    return ans


if __name__ == '__main__':
    main()