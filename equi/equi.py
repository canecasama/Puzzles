#!/usr/bin/env python
"""Equi Puzzle provided by Codility at:
http://codility.com/demo/take-sample-test/

Author: Matheus Victor Brum Soares
Email: caneca@gmail.com
Date: March 7th, 2012

"""

def equi(A):
    """Given a list `A` find the middle point in which the sum of 
    all elements of the left of the list is the same as the sum of all
    elements of the right of the list. If there is no equilibrium point,
    return -1

    Args:
    A -- list of integers

    Returns:
    integer with equilibrium index of the list or -1 if it is not found

    Examples:
    >>> equi([-7, 1, 5, 2, -4, 3, 0])
    3

    """
    # Calculate the sum of the right as zero and the sum of the left
    #  as all elements minus the first
    right = 0
    left = sum(A[1:])

    lenght = len(A) - 1

    for idx in range(len(A)):
        # If the left and right are equals return equilibrium index
        if right == left:
            return idx

        # If the index is going to be out of range, there is no equilibrium
        if lenght < idx + 1:
            return -1

        # Sum next element in the right and subtract from the left
        right += A[idx]
        left -= A[idx + 1]

    # If loop finished, there was no equilibrium index
    return -1

