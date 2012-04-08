#!/usr/bin/env python
"""Magicka Puzzle provided by Google Code Jam at:
http://code.google.com/codejam/contest/975485/dashboard#s=p1

Author: Matheus Victor Brum Soares
Email: caneca@gmail.com
Date: April 8th, 2012

"""
from sys import stdin
import re


def calculate_invokation(combine, opposed, invoked):
    """Invoke the `invoked` list in order from left to right, if the last
    two elements are in the dict `combine` them substitute them for the
    non-base element in the dict, after if there is `opposed` elements
    in the invoke list, clean the list.

    Args:
    combine -- dict with base elements as key and non-base as values
    opposed -- string with regexp to find opposed elements
    invoked -- list with elements to invoke

    Returns:
    list with invoked elements

    Examples:
    >>> calculate_invokation({}, '', ['E', 'A'])
    ['E', 'A']
    >>> calculate_invokation({'QR': 'I', 'RQ': 'I'}, '', ['R', 'R', 'Q', 'R'])
    ['R', 'I', 'R']
    >>> calculate_invokation({'QF': 'T', 'FQ': 'T'}, '(Q.*?F|F.*?Q)',
    ...                      ['F', 'A', 'Q', 'F', 'D', 'F', 'Q'])
    ['F', 'D', 'T']
    >>> calculate_invokation({'EE': 'Z'}, '(Q.*?E|E.*?Q)',
    ...                      ['Q', 'E', 'E', 'E', 'E', 'R', 'A'])
    ['Z', 'E', 'R', 'A']
    >>> calculate_invokation({}, '(Q.*?W|W.*?Q)', ['Q', 'W'])
    []

    """
    invoke = ''
    # Compile the regexp for performance
    regexp = re.compile(opposed)

    for element in invoked:
        # Invoke new element
        invoke += element

        # If there is less than two elements invoked, invoke next
        if len(invoke) < 2:
            continue

        # Check if last 2 elements can combine
        last = invoke[-2:]
        if last in combine:
            # If elements can combine, remove the 2 last elements and
            #  add the combination 
            invoke = invoke[:-2] + combine[last]

        # If there is opposed elements, search for it
        if opposed:
            match = regexp.search(invoke)
            if match:
                # If the opposed elements were added in the list
                #  clean it
                invoke = ''

    return [char for char in invoke]


def parse_input():
    """Parse inputs where `T` is the number of test cases, `C` is the number
    of combine elements followed by `C` 3-char elements, `D` is the number
    of opposed elements followed by `D` 2-char elements, and `N` is the
    number of elements to invoke followed by `N`-char elements

    Returns:
    array of 2-tuples like: [(`N`, `RP`), ...]
    
    """
    T = int(stdin.readline().strip())
    
    elements = []
    for idx in xrange(T):
        line = stdin.readline().strip().split(' ')

        C = int(line.pop(0))

        # Generate dictionary with all combine elements
        combine = {}
        for idx_c in xrange(C):
            combination = line.pop(0)
            combine.update({
                combination[:2]: combination[-1],
                '{1}{0}'.format(*combination[:2]): combination[-1]
            })

        D = int(line.pop(0))

        # Generate regexp with all opposed elements
        opposed = []
        for idx_d in xrange(D):
            opposition = line.pop(0)
            opposed.append('{0}.*?{1}|{1}.*?{0}'.format(*opposition))

        opposed = '({0})'.format('|'.join(opposed))
        if opposed == '()':
            opposed = ''

        N = int(line.pop(0))
        # Generate list with elements to be invoked
        invoked = [char for char in line.pop(0)]

        elements.append((combine, opposed, invoked))

    return elements


def main():
    elements = parse_input()

    idx = 1
    for element in elements:
        result = calculate_invokation(*element)
        result = ', '.join(result)
        print 'Case #{0}: [{1}]'.format(idx, result)
        idx += 1


if __name__ == '__main__':
    main()
