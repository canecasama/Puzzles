#!/usr/bin/env python
"""Snapper Chain Puzzle provided by Google Code Jam at:
http://code.google.com/codejam/contest/433101/dashboard#s=p0

Author: Matheus Victor Brum Soares
Email: caneca@gmail.com
Date: April 9th, 2012

"""
from sys import stdin


def calculate_power(N, K):
    """Check if the power will be 'ON' or 'OFF' depending on the amount `N `
    of snappers there are in the chain and the amount `K` of times you
    snap your fingers. The power will just be on if at the end ALL snappers
    in the chain are 'ON'

    Args:
    N -- integer with number of snappers
    K -- integer with number of times you snap your finger

    Returns:
    'ON' if all snappers are 'ON', 'OFF' otherwise

    Examples:
    >>> calculate_power(1, 0)
    'NO'
    >>> calculate_power(1, 1)
    'YES'
    >>> calculate_power(4, 0)
    'NO'
    >>> calculate_power(4, 47)
    'YES'

    """
    times_switched = [K,]

    for idx in xrange(1, N):
        # Every chained snapper switches half of the time of its parent
        #  calculate how many times each snapper switches the power
        times_switched.append(times_switched[-1] / 2)
    
    # The snapper are 'ON' if it have a odd number of switches.
    #  If all snappers have odd numbers, then the light is 'ON'
    return 'ON' if all(map(lambda num: num % 2, times_switched)) else 'OFF'


def parse_input():
    """Parse inputs where `T` is the number of test cases, `N` is the number
    of snapper devices, and `K` is the number of times you snap your fingers

    Returns:
    array of 2-tuples like: [(`N`, `K`), ...]
    
    """
    T = int(stdin.readline().strip())
    
    snappers = []
    for idx in xrange(T):
        (N, K) = map(int, stdin.readline().strip().split(' '))
        snappers.append((N, K))

    return snappers


def main():
    snappers = parse_input()

    idx = 1
    for snapper in snappers:
        result = calculate_power(*snapper)
        print 'Case #{0}: {1}'.format(idx, result)
        idx += 1


if __name__ == '__main__':
    main()
