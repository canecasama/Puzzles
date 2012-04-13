#!/usr/bin/env python
"""Theme Park Puzzle provided by Google Code Jam at:
http://code.google.com/codejam/contest/433101/dashboard#s=p2

Author: Matheus Victor Brum Soares
Email: caneca@gmail.com
Date: April 12th, 2012

"""
from sys import stdin


def calculate_money(R, k, g):
    """Check how much money the roller coaster will make, when each ride costs
    1 Euro and the people after riding the roller coster go back to the line.

    Args:
    R -- integer with number of times the roller coster will run
    k -- integer with number of people it fits at once
    g -- list of integers with number of people in each group

    Returns:
    integer with number or euros gained this day

    Examples:
    >>> calculate_money(4, 6, [1, 4, 2, 1])
    21
    >>> calculate_money(100, 10, [1])
    100
    >>> calculate_money(5, 5, [2, 4, 2, 3, 4, 2, 1, 2, 1, 3])
    20

    """
    start = idx = 0
    length = len(g)
    amount = []
    visited = []

    while idx < R:
        # It this index was already visited it means that a loop will start
        if start in visited:
            # Check the index where the loop starts
            #  it can happen that the loop don't start in the index 0
            loop_idx = visited.index(start)
            # Get the length of the loop and the lenght before the loop
            loop_length = len(amount[loop_idx:])
            begin_length = len(amount[:loop_idx])

            # Calculate how many loops where done and how many rides still
            #  missing to complete the amount of rides of the day
            multiplier = (R - begin_length) / loop_length
            reminder = (R - begin_length) % loop_length

            # Get the begin of the list before the loop start
            amount_begin = amount[:loop_idx]
            # Calculate how much is earned in the loop
            amount_loop = sum(amount[loop_idx:]) * multiplier
            # Add begin and loop together
            amount = amount_begin + [amount_loop]

            # Update index to run the rides that still missing to
            #  complete the day
            idx = R - reminder
            visited = []

        else:
            # Check how many groups can fit in the roller coster 
            #  and add in a list
            ride = 0

            for idx_g in xrange(start, start + length):
                idx_g = idx_g % length
                if ride + g[idx_g] > k:
                    break
                ride += g[idx_g]

            # Mark the start index as visited to check later for loops 
            visited.append(start)
            amount.append(ride)
            # Next iteration the line will start from the first group
            #  not selected
            start = idx_g

            idx += 1

    # Return the sum of the amount for all rides
    return sum(amount)


def parse_input():
    """Parse inputs where `T` is the number of test cases, `R` is the number
    of runs of the roller coster, `k` is the number of people that fits at
    once, `N` is the number of groups in the line to use the roller coster,
    and `g` is the list with the groups

    Returns:
    array of 3-tuples like: [(`R`, `k`, [`g`]), ...]

    """
    T = int(stdin.readline().strip())
    
    rides = []
    for idx in xrange(T):
        (R, k, N) = map(int, stdin.readline().strip().split(' '))
        g = map(int, stdin.readline().strip().split(' '))
        rides.append((R, k, g))

    return rides


def main():
    rides = parse_input()

    idx = 1
    for ride in rides:
        result = calculate_money(*ride)
        print 'Case #{0}: {1}'.format(idx, result)
        idx += 1


if __name__ == '__main__':
    main()
