#!/usr/bin/env python
"""Candy Splitting Puzzle provided by Google Code Jam at:
http://code.google.com/codejam/contest/975485/dashboard#s=p2

Author: Matheus Victor Brum Soares
Email: caneca@gmail.com
Date: April 7th, 2012

"""
from sys import stdin


def calculate_bag(num_candies, candies):
    """Calculate the sum and the xor of the lists in order to give the biggest
    sum of elements where the xor is the same.

    Args:
    num_candies -- size of list
    candies     -- list with candies numbers

    Returns:
    integer with biggest bag of candies or `NO` if none is found

    Examples:
    >>> calculate_bag(5, [1, 2, 3, 4, 5])
    'NO'
    >>> calculate_bag(3, [3, 5, 6])
    11

    """
    # Sort the candies
    candies.sort()

    # Calculate the xor of all elements
    xor_left = xor_right = 0
    for candy in candies:
        xor_right ^= candy

    # Calculate the sum of all elements
    sum_left = 0
    sum_right = sum(candies)

    for idx in xrange(num_candies):
        candy = candies[idx]

        # Calculate xor for the right and left
        xor_left ^= candy
        xor_right ^= candy

        # Increase left list and decrease right list
        sum_left += candy
        sum_right -= candy

        # If both lists have same xor result return
        if xor_left == xor_right:
            return max(sum_left, sum_right)

    # There was no solution for this candies
    return 'NO'


def parse_input():
    """Parse inputs where `T` is the number of test cases, `N` is the number
    of candies in the bag and `C` is a array with the values in each candy

    Returns:
    array of 2-tuples like: [(`N`, `C`), ...]
    
    """
    T = int(stdin.readline().strip())
    
    candies = []
    for idx in xrange(T):
        N = int(stdin.readline().strip())
        C = map(int, stdin.readline().strip().split(' '))
        candies.append((N, C))

    return candies


def main():
    candies = parse_input()

    idx = 1
    for candy in candies:
        result = calculate_bag(*candy)
        print 'Case #{0}: {1}'.format(idx, result)
        idx += 1


if __name__ == '__main__':
    main()
