#!/usr/bin/env python
"""Dancing with the Googlers Puzzle provided by Google Code Jam at:
https://code.google.com/codejam/contest/1460488/dashboard#s=p1

Author: Matheus Victor Brum Soares
Email: caneca@gmail.com
Date: April 14th, 2012

"""
from sys import stdin


def calculate(S, p, t):
    """Get the total score of the Googlers split into the tree judges
    and get the maximum number of Googlers that have a judged score
    greater or equals to `p` where the diference between one judge
    and another is no greater than 1 in the normal cases, and for `S`
    Googlers the surprising differente of 2.

    Args:
    S -- integer with surprise numbers in the list
    p -- integer with minumum score to be archieved
    t -- list of integers with total scores

    Returns:
    integer with number of scores greater or equals to `p`

    Examples:
    >>> calculate(1, 5, [15, 13, 11])
    3
    >>> calculate(0, 8, [23, 22, 21])
    2
    >>> calculate(1, 1, [8, 0])
    1
    >>> calculate(2, 8, [29, 20, 8, 18, 18, 21])
    3
    >>> calculate(0, 8, [23, 22, 21] * 33)
    66
    >>> calculate(2, 8, [29, 20, 8, 18, 18, 21] * 16)
    18
    >>> calculate(5, 7, range(31) * 3)
    41

    """
    count = 0

    for num in t:
        # Get the medium point the judges used
        div = num / 3
        # Get the reminder points to decide where and how to use it later
        rem = num % 3

        # If the medium score is already greater or equal to `p`
        #  increment count
        if div >= p:
            count += 1

        # If there is points left to divide between the judges
        #  and using one it will be greater or equal to `p`, increment 
        elif rem >= 1 and div + 1 >= p:
            count += 1

        # If still surprising scores left try to use it
        elif S:
            # Two ways to use a surprising score is:
            #  * to have 2 points left to divide between the judges and put
            #    it all in one judge.
            #  * remove one point from one judge and add in the other
            #  if any of those cases can come with a result greater or equal
            #  to `p`, increment count
            if (rem == 2 and div + rem >= p) \
                or (rem == 0 and div != 0 and div + 1 >= p):
                S -= 1
                count += 1

    return count


def parse_input():
    """Parse inputs where `T` is the number of test cases, `N` is the
    number of Googlers, `S` is the number of surprises, `p` is the 
    minimum score to be archieved, and `t` is a list with total points
    of each Googler `N`

    Returns:
    array of 3-tuples like: [(`S`, `p`, [`t`]), ...]
    
    """
    T = int(stdin.readline().strip())
    
    result = []
    for idx in xrange(T):
        t = map(int, stdin.readline().strip().split(' '))
        N = t.pop(0)
        S = t.pop(0)
        p = t.pop(0)
        result.append((S, p, t))

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
