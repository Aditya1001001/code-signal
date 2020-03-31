"""Given a string s consisting of small English letters, find and return the first
instance of a non-repeating character in it. If there is no such character, return '_'.

asked by - Amazon

Example:
For s = "abacabad", the output should be firstNotRepeatingCharacter(s) = 'c'.
There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

For s = "abacabaabacaba", the output should be
firstNotRepeatingCharacter(s) = '_'.
There are no characters in this string that do not repeat. """

def firstNotRepeatingCharacter(s):
    l ={}
    for x in s:
        if x not in l:
            l[x] = 1
        else:
            l[x] += 1
    for x in s:
        if l[x] == 1:
            return x
    else:
        return "_"


# for c in s:
#         if s.index(c) == s.rindex(c):
#             return c
#     return '_'