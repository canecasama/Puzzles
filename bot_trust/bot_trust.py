#!/usr/bin/env python
"""Bot Trust Puzzle provided by Google Code Jam at:
http://code.google.com/codejam/contest/975485/dashboard#s=p0

Author: Matheus Victor Brum Soares
Email: caneca@gmail.com
Date: April 7th, 2012

"""
from sys import stdin


def calculate_seconds(num_buttons, buttons):
    """Calculate how many seconds two robots can press a sequency of
    buttons in the right order where walk from one button to the next,
    wait idle in a button or press a button all takes 1 second each.

    Args:
    num_buttons -- number of buttons to press
    button      -- list of 2-tuples like: [(robot, button), ...]

    Returns:
    minimum of seconds to complete the task

    Examples:
    >>> calculate_seconds(4, [('O', 2), ('B', 1), ('B', 2), ('O', 4)])
    6
    >>> calculate_seconds(3, [('O', 5), ('O', 8), ('B', 100)])
    100
    >>> calculate_seconds(2, [('B', 2), ('B', 1)])
    4
    >>> calculate_seconds(6, [('O', 14), ('B', 16), ('O', 37),
    ...                       ('B', 37), ('O', 7), ('B', 66)])
    70

    """
    # Inicial possition of the robots
    b = o = 1

    # Buffer of moviments
    buffer_b = buffer_o = 0
    # Seconds taken
    time = 0

    for button in buttons:
        # Get initial possition of the robot and clean the buffer
        if button[0] == 'O':
            position = o
            o = button[1]
            buff = buffer_o
            buffer_o = 0
        else:
            position = b
            b = button[1]
            buff = buffer_b
            buffer_b = 0
        
        # How many buttons the robot need to walk
        walk = max(position, button[1]) - min(position, button[1])
        # Add one (which is the pressing button action)
        #  and remove from the buffer 
        buff -= walk + 1

        # If the buffer is negative, it means it took more time than
        #  what was in the buffer to walk to the next button and press it
        #  so add the extra time necessary. If the buffer is not negative,
        #  it means the robot just need to press the button, so add
        #  one second to the time
        if buff < 0:
            time += abs(buff)
            extra_buffer = abs(buff)
        else:
            time += 1
            extra_buffer = 1

        # Add the extra buffer time to the other robot
        if button[0] == 'O':
            buffer_b += extra_buffer
        else:
            buffer_o += extra_buffer

    return time


def parse_input():
    """Parse inputs where `T` is the number of test cases, `N` is the number
    of buttons to be pressed, `RP` is an arrays with the values of
    each button

    Returns:
    array of 2-tuples like: [(`N`, `RP`), ...]
    
    """
    T = int(stdin.readline().strip())
    
    candies = []
    for idx in xrange(T):
        line = stdin.readline().strip().split(' ')

        N = int(line[0])
        RP = [(line[idx * 2 - 1], int(line[idx * 2]))
             for idx in xrange(1, N + 1)]

        candies.append((N, RP))

    return candies


def main():
    buttons = parse_input()

    idx = 1
    for button in buttons:
        result = calculate_seconds(*button)
        print 'Case #{0}: {1}'.format(idx, result)
        idx += 1


if __name__ == '__main__':
    main()
