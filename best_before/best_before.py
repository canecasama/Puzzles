#!/usr/bin/env python
"""Best Before Puzzle provided by Spotify at:
http://www.spotify.com/se/jobs/tech/best-before

Author: Matheus Victor Brum Soares
Email: caneca@gmail.com
Date: March 18th, 2012

"""
from sys import stdin
from datetime import date
from itertools import permutations


def best_before(date_str):
    """Calculate the minimum valid date.

    Args:
    date_str -- string containing the date to be calculated

    Return:
    minimum valid date if exists, else string informing there is no valid date

    Examples:
    >>> best_before('02/4/67')
    '2067-02-04'
    >>> best_before('31/9/73')
    '31/9/73 is illegal'
    >>> best_before('5/1950/4')
    '5/1950/4 is illegal'
    >>> best_before('12/30/200')
    '2200-12-30'
    >>> best_before('1/02/0')
    '2000-01-02'
    >>> best_before('29/02/100')
    '29/02/100 is illegal'

    """
    def map_date(date_list):
        """Returns valid date or False"""
        try:
            # If year was represented in a number smaller than 2000, fix it
            if date_list[0] < 2000:
                year = date_list[0] + 2000
            else:
                year = date_list[0]

            result = date(year, date_list[1], date_list[2])

            # Check if date is in the legal range and return it
            if date(2000, 1, 1) <= result <= date(2999, 12, 31):
                return result

            return False
        except ValueError:
            return False
            
    # Map each number in the string into a integer
    date_list = map(int, date_str.split('/'))
    # Get all possible dates with those numbers
    dates = permutations(date_list)
    # Detect dates
    dates = map(map_date, dates)
    # Filter out invalid dates
    dates = filter(None, dates)

    try:
        # Get minimum date
        min_date = min(dates)
    except ValueError:
        # If no dates provided, the string contained no valid dates
        return "{0} is illegal".format(date_str)

    return min_date.strftime("%Y-%m-%d")


if __name__ == '__main__':
    print best_before(stdin.readline().strip())

