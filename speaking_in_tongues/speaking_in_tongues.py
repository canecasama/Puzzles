#!/usr/bin/env python
"""Speaking in Tongues Puzzle provided by Google Code Jam at:
https://code.google.com/codejam/contest/1460488/dashboard#s=p0

Author: Matheus Victor Brum Soares
Email: caneca@gmail.com
Date: April 14th, 2012

"""
from sys import stdin

#Translation dictionary generated manually using the puzzle information:
# 'a' -> 'y', 'o' -> 'e', and 'z' -> 'q'
#
# ejp mysljylc kd kxveddknmc re jsicpdrysi
# rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
# de kr kd eoya kw aej tysr re ujdr lkgc jv
#
# our language is impossible to understand
# there are twenty six factorial possibilities
# so it is okay if you want to just give up
TRANSLATION = {
    'a': 'y',
    'b': 'n',
    'c': 'f',
    'd': 'i',
    'e': 'c',
    'f': 'w',
    'g': 'l',
    'h': 'b',
    'i': 'k',
    'j': 'u',
    'k': 'o',
    'l': 'm',
    'm': 'x',
    'n': 's',
    'o': 'e',
    'p': 'v',
    'q': 'z',
    'r': 'p',
    's': 'd',
    't': 'r',
    'u': 'j',
    'v': 'g',
    'w': 't',
    'x': 'h',
    'y': 'a',
    'z': 'q',
}

# Swapping key and value so the key is the Googlerese and the value the English
TRANSLATION = dict([(char[1], char[0]) for char in TRANSLATION.items()])

def calculate(G):
    """Translate Googlerese to English using the `TRANSLATION` dict

    Args:
    G -- list with each word of the phrase in Googlerese

    Returns:
    string with text in translated to English

    Examples:
    >>> calculate(['ejp', 'mysljylc', 'kd', 'kxveddknmc', 're', 'jsicpdrysi'])
    'our language is impossible to understand'
    >>> calculate(['rbcpc', 'ypc', 'rtcsra', 'dkh',
    ...            'wyfrepkym', 'veddknkmkrkcd'])
    'there are twenty six factorial possibilities'
    >>> calculate(['de', 'kr', 'kd', 'eoya', 'kw', 'aej', 'tysr',
    ...            're', 'ujdr', 'lkgc', 'jv'])
    'so it is okay if you want to just give up'

    """
    result = []

    for word in G:
        # Translate each word
        result.append(''.join([TRANSLATION[char] for char in word]))

    # Join all words back to a string
    return ' '.join(result)


def parse_input():
    """Parse inputs where `T` is the number of test cases, ang `G` is the
    text in Googlerese

    Returns:
    array of arrays like: [[every word in `G`], ...]
    
    """
    T = int(stdin.readline().strip())
    
    result = []
    for idx in xrange(T):
        G = stdin.readline().strip().split(' ')
        result.append((G))

    return result


def main():
    result = parse_input()

    idx = 1
    for test in result:
        answer = calculate(test)
        print 'Case #{0}: {1}'.format(idx, answer)
        idx += 1


if __name__ == '__main__':
    main()
