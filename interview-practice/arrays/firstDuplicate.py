""" Given an array a that contains only numbers in the range from 1 to a.length,
find the first duplicate number for which the second occurrence has the minimal index.
In other words, if there are more than 1 duplicated numbers, return the number for which
the second occurrence has a smaller index than the second occurrence of the other number does.
If there are no such elements, return -1.

asked by - Google

Example:
For a = [2, 1, 3, 5, 3, 2], the output should be firstDuplicate(a) = 3.
For a = [2, 2], the output should be firstDuplicate(a) = 2;
For a = [2, 4, 3, 5, 1], the output should be firstDuplicate(a) = -1."""

def firstDuplicate(a):
    l ={}
    for x in a:
        if str(x) not in l:
            l[str(x)] = 1
        else:
            return x
    else:
        return -1