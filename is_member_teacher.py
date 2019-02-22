"""
is_member.py: Recursive implementation of is_member() on a set
              represented by a sorted list of integers
Authors: jsventek (Joe Sventek)

CIS 210 assignment 4, part 1, Fall 2015. 
"""
import argparse      # Used in main program to obtain command arguments
from test_harness import testEQ  # Used in CIS 210 for test cases 

## Constants used by this program

def gen_set(set_file):
    """
    Generates a sorted list representing the set of integers obtained from
    a file

    Inputs:
        set_file - an open file object containing integer elements of a
            set, one per line; guaranteed that there are no empty lines,
            or duplicate elements in the file
    Outputs:
        returns a sorted list of the integer elements obtained from the file
    """
    the_set = []
    for line in set_file:
        the_set.append(int(line.strip()))
    the_set.sort()
    return the_set

def is_member(set, number):
    """
    Given a sorted list representing a set of integers, and an integer,
    determines if that integer is a member of the set

    Inputs:
        set - a sorted list of integers making up a set
        number - the integer for which we desire membership information
    Returns:
        returns True if number is an element of set
        returns False if number is not an element of set
    """
    top = len(set)
    if top == 0:		# passed an empty set
        return False
    mid = top // 2
    if number == set[mid]:	# success basis case
        return True
    if number > set[mid]:
        left = mid + 1
        right = top
    else:
        left = 0
        right = mid
    if left >= right:		# failure basis case
        return False
    return is_member(set[left:right], number)	# progress case

def run_tests():
    """
    This function runs a set of tests to help you debug your
    program as you develop it.
    """
    l = [-27, -12, -5, -1, 0, 2, 3, 6, 8, 10, 13, 25, 46, 99]
    print("**** TESTING --- Check membership of locally-defined set")
    print(l)
    testEQ("-99 is False", is_member(l, -99), False)
    testEQ("115 is False", is_member(l, 115), False)
    testEQ("-27 is True", is_member(l, -27), True)
    testEQ("99 is True", is_member(l, 99), True)
    testEQ("0 is True", is_member(l, 0), True)
    testEQ("-4 is False", is_member(l, -4), False)
    testEQ("14 is False", is_member(l, 14), False)
    testEQ("42 is not a member of an empty set", is_member([], 42), False)
    print("*** End of provided test cases.  Add some of your own? ****")

def main():
    """
    Interaction if run from the command line.
    """
    parser = argparse.ArgumentParser(description="Recursive implementation of is_member()")
    parser.add_argument("set", type=argparse.FileType('r'),
                        help="A text file containing set elements, one per line.")
    parser.add_argument("number", type=int, help="number to check for membership")
    args = parser.parse_args()  # gets arguments from command line
    set_file = args.set
    number = args.number
    the_set = gen_set(set_file)
    if is_member(the_set, number):
        print(number, "is an element of the set")
    else:
        print(number, "is not an element of the set")

if __name__ == "__main__":
    # run_tests()  # Comment this out when your program is working
    main()     # Uncomment this when your program is working



