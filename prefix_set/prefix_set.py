#!/usr/bin/env python
"""Prefix Set Puzzle provided by Codility at:
http://codility.com/demo/take-sample-test/ps/

Author: Matheus Victor Brum Soares
Email: caneca@gmail.com
Date: March 7th, 2012

"""

def ps(A):
    """Given a list `A` find the first prefix of the list in which all the
    different elements are covered.

    Args:
    A -- list of integers

    Returns:
    integer with index of the first covering prefix in the list

    Examples:
    >>> ps([2, 2, 1, 0, 1])
    3

    """
    # Get all different elements of A
    B = set(A)

    for idx in range(len(A)):
        # Sucessively remove from the set the elements of the list
        if A[idx] in B:
            B.remove(A[idx])
    
        # If the set is empty it means you found the index where all elements
        #  are covered.
        if len(B) == 0:
            return idx

