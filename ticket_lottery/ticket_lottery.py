#!/usr/bin/env python
"""Ticket Lottery Puzzle provided by Spotify at:
http://www.spotify.com/se/jobs/tech/ticket-lottery

Author: Matheus Victor Brum Soares
Email: caneca@gmail.com
Date: March 18th, 2012

"""
from sys import stdin
from math import ceil


def calc_probability(m, n, p, x):
    """Calculate the probability that with `p` lottery tickets 
    you win `x` times from `n` draws with `m` tickets in the lottery.

    Args:
    m -- total number of people
    n -- total number of winners
    p -- number of people in the group
    x -- number of times you win

    Returns:
    float with probability

    Examples:
    >>> print "{0:.5f}".format(calc_probability(52, 26, 5, 2))
    0.32513
    >>> print "{0:.6f}".format(calc_probability(100, 6, 10, 5))
    0.000019
    >>> print "{0:.12f}".format(calc_probability(60, 6, 6, 4))
    0.000428752397
    >>> print "{0:.1f}".format(calc_probability(60, 60, 60, 30))
    0.0

    """
    def combination(x, y):
        """Calculate the combination of `x`, `y` to `y`: C^{x}_{y}"""
        if y > x:
            return 0.0

        z = x - y
        numerator = denominator = 1

        # Since the biggest factorial in the denominator will cancel
        #  with part of the numerator in the division, it is not
        #  necessary to calculate it. Calculate instead, just what
        #  is left of the numerator and the smallest factorial in
        #  the denominator
        for idx in xrange(1, min(y, z) + 1):
            numerator *= x
            denominator *= idx
            x -= 1

        return float(numerator / denominator)

    return combination(n, x) * combination(m - n, p - x) / combination(m, p)


def ticket_lottery(lottery_str):
    """Calculate the minimum valid date.

    Args:
    lottery_str -- string containing m total number of people,
                   n total number of winners,
                   t number of tickets winners can buy,
                   p number of people in the group.

    Return:
    probability that entire group can get tickets

    Examples:
    >>> ticket_lottery('100 10 2 1')
    '0.1000000000'
    >>> ticket_lottery('100 10 2 2')
    '0.1909090909'
    >>> ticket_lottery('10 10 5 1')
    '1.0000000000'
    >>> ticket_lottery('100 1 2 3')
    '0.0000000000'
    >>> ticket_lottery('50 5 2 5')
    '0.0047792104'
    >>> ticket_lottery('60 60 2 60')
    '1.0000000000'

    """
    # Parse input into the variables requested in the puzzle
    (m, n, t, p) = map(int, lottery_str.split(' '))

    # Minimum number of times you need to win to buy tickets to all your group
    min_winners = int(ceil(float(p) / t))

    # If it is necessary to have more winners than the total
    #  amount of winners, the probability is zero
    if min_winners > n:
        return '{0:.10f}'.format(0.0)

    probability = 0.0

    # Calculate the cumulative probability
    for idx in range(min_winners, n + 1):
        if idx > p:
            break

        probability += calc_probability(m, n, p, idx)

    # Format the output.
    #  Using `.11f` and `[:12]` because python rounds up the last decimal
    #  if just `.10f` is used. So like this the rounded decimal is striped
    #  out not losing the precision asked
    return '{0:.11f}'.format(probability)[:12]


if __name__ == '__main__':
    print ticket_lottery(stdin.readline().strip())

