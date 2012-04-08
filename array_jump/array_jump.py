#!/usr/bin/env python
"""Array Jump Puzzle provided by Codility.

Author: Matheus Victor Brum Soares
Email: caneca@gmail.com
Date: March 10th, 2012

"""

def arrayJmp(A):
    """Given a list `A` jump from one index to another using the formula
    next_index = current_index + A[current_index]. Count the times you need
    to jump to leave the list. If you never leave the list return -1

    Args:
    A -- list of integers

    Returns:
    integer with number of jumps, or -1 if never leave the list

    Examples:
    >>> arrayJmp([2, 3, 1, 1, 3])
    4
    >>> arrayJmp([1, 1, -1, 1])
    -1

    """
    visited = set()
    length = len(A)
    count = idx = 0
   
    # Iterate while the index is inside the list range
    while 0 <= idx < length:
        # If tou visit twice the same index it means you will never
        #  leave the list
        if idx in visited:
            return -1
          
        # Mark the index as visited, calculate the next jump and count +1  
        visited.add(idx)
        idx = idx + A[idx]
        count += 1
        
    return count


