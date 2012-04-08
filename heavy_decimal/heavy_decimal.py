#!/usr/bin/env python
"""Heavy Decimal Puzzle provided by Codility.

Author: Matheus Victor Brum Soares
Email: caneca@gmail.com
Date: March 10th, 2012

"""
from operator import add


def heavyDecimal(A, B):    
    """Given two numbers `A` and `B` calculate for the inclusive range
    `A` to `B` how many heavy numbers are there. A heavy number is calculated
    by the sum of each digit of the number divided by the number of digits,
    if the result is greater than 7 it is a heavy number.

    Args:
    A -- integer begin of the range
    B -- integer end of the range

    Returns:
    integer with amount of heavy numbers in the range

    Examples:
    >>> heavyDecimal(8675, 8689)
    5

    """
    count = 0

    # The range is inclusive so need to add `B` into the range
    for number in xrange(A, B + 1):
        # Map every digit of the number to a separeted integer,
        #  reduce it with the sum operation, and
        #  divide by the length of the number
        result = reduce(add, map(int,
                                 str(number))) / float(len(str(number)))

        # If the result is greater then 7, count it
        if result > 7:
            count += 1

    return count


