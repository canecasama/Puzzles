#!/usr/bin/env python
"""Number of Disc Intersections Puzzle provided by Codility at:
http://codility.com/demo/take-sample-test/ndi/

Author: Matheus Victor Brum Soares
Email: caneca@gmail.com
Date: March 9th, 2012

"""
from math import sqrt


def sqrt_search(element, array):
    """Square root search divides a ordered list `array` where all elements
    on the left are smaller than `element` and all elements in the right are
    greater than `element`. First set a step for the search in which the
    primary search will be done from step to step instead of one by one
    after find in which partition of the `array` the `element` is. Later
    search one by one just inside the small partition by the `element`.
    NOTE: This search was adapted to work with 2-tuples where `element`[1]
    should be greater than `array`[n][0]

    Time complexity is O(sqrt(n))

    Args:
    element -- where you want to divide the list
    array   -- ordered list with numbers

    Return:
    integer with number of elements in the left of the list 

    Examples:
    >>> sqrt_search((0, 1), [(0, 4), (0, 5), (0, 5), (2, 4), (5, 5)])
    3
    >>> sqrt_search((5, 5), [])
    0

    """
    length = len(array)
    # Set the steps of the search
    step = int(sqrt(length + 1))

    # Find in which partition the `element` should be
    start = 0
    for idx in xrange(step, length, step):
        if element[1] < array[idx][0]:
            break
        start = idx

    # After having the start of the partition, set the end of it as well
    end = start + step
    if end > length:
        end = length

    # Find in the partition the actual index that satisfy the search
    index = start
    for idx in xrange(start, end):
        if element[1] < array[idx][0]:
            break
        index = idx
    
    # Returns the number of elements until the `index`
    return index + 1 if index != 0 else index


def number_of_disc_intersections(A):
    """From a list of integers `A` find the number of intersections of the
    discs where `A`[n] is a radius of the disc and n is the center of the
    disc.

    Args:
    A -- list of integers with radius of the discs

    Returns:
    integer with the count of intersections

    Examples:
    >>> number_of_disc_intersections([1, 5, 2, 1, 4, 0])
    11

    """
    def get_pos(radius, idx):
        """Set the left and right radius of the circle respecting the
        limits of the array.

        Args:
        radius -- integer radius of the circle
        idx    -- integer the center point of the circle
        
        Returns:
        integer where the circle ocuppy in the array        

        """
        if radius + idx < 0:
            return 0

        elif radius + idx > len(A) - 1:
            return len(A) - 1

        return radius + idx

    # Set and sort the list of 2-tuples with the radius of the circles
    B = [(get_pos(-abs(A[idx]), idx), get_pos(abs(A[idx]), idx))
         for idx in range(len(A))]
    B = sorted(B, key=lambda c: (c[0], c[1]))

    # Count the intersections
    intersections = 0
    for idx in range(len(B)):
        intersections += sqrt_search(B[idx], B[idx + 1:])

        # If more than 10kk intersections return -1
        if intersections > 10000000:
            return -1 

    # Return number of intersections
    return intersections

