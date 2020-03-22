"""Implement a function that can reduce a fraction.

Example-
For fraction = [2, 6], the output should be
fractionReducing(fraction) = [1, 3];
For fraction = [4, 1], the output should be
fractionReducing(fraction) = [4, 1]. """

def fractionReducing(fraction):
    hcf = 1
    for i in range(2, min(fraction) + 1):
        if fraction[0] % i == 0 and fraction[1] % i == 0:
            hcf = i
    return [ i / hcf for i in fraction]