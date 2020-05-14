"""A little boy is studying arithmetics. He has just learned how to add two
integers, written one below another, column by column. But he always forgets
about the important part - carrying. 
Given two integers, your task is to find the result which the little boy will
get.

Note: The boy had learned from this site, so feel free to check it out too if
you are not familiar with column addition.

Example

For param1 = 456 and param2 = 1734, the output should be
additionWithoutCarrying(param1, param2) = 1180. """

def additionWithoutCarrying(param1, param2):
    res = []
    if param1 == 0 and param2 == 0:
        return 0
    while param1 > 0 or param2 > 0:
        a = param1 % 10
        b = param2 % 10
        param1 = int(param1/ 10)
        param2 = int(param2/ 10)
        res.append(str((a + b) % 10))
    return int("".join(res[::-1]))
