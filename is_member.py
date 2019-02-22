"""
is_member.py: Recursive implementation of is_member() on a set
              represented by a sorted list of integers
Authors: Nolan Cassidy

CIS 210 assignment 5, part 2, Fall 2016. 
"""
import argparse      # Used in main program to get PIN code from command line
from test_harness import testEQ  # Used in CIS 210 for test cases 

## Constants used by this program

def gen_set(set_file):
    """
    Goes through a file containg integers on seperate lines and add it to a set then returns it sorted

    Args: set_file is the text document containing the integers

    Prints: Nothing

    Returns: sorted list of all elements with in the text document
    """
    the_set = []

    for line in set_file:
        the_set.append(int(line))

    return sorted(the_set)

def is_member(set, number):
    """
    Takes the sorted set and compares it with the number wanting to be checked for. It will continue to half the list until the element is equal to
    the number or the list is empty

    Args: set is a sorted list of integers
          number is the integer being checked for

    Prints: Nothing

    Returns: True if number is in set and False if it is not found
    """
    if len(set)== 0:
        return False
    if number<set[len(set)//2]:
        return is_member(set[:len(set)//2],number)
    elif number > set[len(set) // 2]:
        return is_member(set[len(set)//2+1:],number)
    elif set[len(set)//2] == number:
        return True
    return False

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
    #run_tests()
    main()     



