#!/usr/bin/env python
"""Recycled Numbers Puzzle provided by Google Code Jam at:
https://code.google.com/codejam/contest/1460488/dashboard#s=p2

Author: Matheus Victor Brum Soares
Email: caneca@gmail.com
Date: April 14th, 2012

"""
from sys import stdin
from math import log10


def calculate(A, B):
    """Get the number of recycled numbers between `A` and `B`. A recycled
    numbers are a 2-tuple of numbers where switching any number of digits
    from they still in the specified range. For example 123 and 312 are
    recycled numbers because we switch the 3 from the end of the number
    to the begin

    Args:
    A -- integer where the recycled numbers start
    B -- integer where the recycled numbers end

    Returns:
    integer with number of recycled numbers in the interval `A` to `B`

    Examples:
    >>> calculate(1, 9)
    0
    >>> calculate(10, 40)
    3
    >>> calculate(100, 500)
    156
    >>> calculate(1111, 2222)
    287
    >>> calculate(1000000, 2000000)
    299997
    >>> calculate(100000, 200000)
    24930

    """
    count = 0
    # Calculate just once the multiplier which is a 
    #  1 follow by len(NUMBER) - 1 zeros
    default_multiplier = 10 ** int(log10(A))

    for num in xrange(A, B + 1):
        # A set with the possible recycled numbers
        possible = set()
        # Set start of divisor and multiplier
        divisor = 10
        multiplier = default_multiplier

        # Look until the divisor is bigger than the current number
        while divisor <= num:
            # Get left and right part of the number
            left = num / divisor
            right = num % divisor
            # Get the new recycled number switching left by right and
            # multiplying the right by a multiple of 10 to add the
            # right amount of tailing zeros
            new = right * multiplier + left

            # The new number need to be between the current number and `B`
            # because smaller numbers were already matched with their
            # recycled numbers. The new number cannot be equal to the
            # current number.
            if num < new <= B:
                possible.add(new)

            # Increase divisor and decreade multiplier
            divisor *= 10
            multiplier /= 10

        # Count how many numbers where matched
        count += len(possible)

    return count


def parse_input():
    """Parse inputs where `T` is the number of test cases, and `A` and `B`
    are two integers with the same number of digits and no leading zeros.

    Returns:
    array of 2-tuple like: [(`A`, `B`), ...]
    
    """
    T = int(stdin.readline().strip())
    
    result = []
    for idx in xrange(T):
        (A, B) = map(int, stdin.readline().strip().split(' '))
        result.append((A, B))

    return result


def main():
    result = parse_input()

    idx = 1
    for test in result:
        answer = calculate(*test)
        print 'Case #{0}: {1}'.format(idx, answer)
        idx += 1


if __name__ == '__main__':
    main()
