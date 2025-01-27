""" Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s.

Example:
For inputString = "(bar)", the output should be
reverseInParentheses(inputString) = "rab";
For inputString = "foo(bar)baz", the output should be
reverseInParentheses(inputString) = "foorabbaz";
For inputString = "foo(bar)baz(blim)", the output should be
reverseInParentheses(inputString) = "foorabbazmilb";
For inputString = "foo(bar(baz))blim", the output should be
reverseInParentheses(inputString) = "foobazrabblim".
Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim". """


def reverseInParentheses(s):
    # return eval('"' + s.replace('(', '"+("').replace(')', '")[::-1]+"') + '"')
    stack = []
    for x in s:
        if x == ")":
            temp = ""
            while stack[-1] != "(":
                temp += stack.pop()
            stack.pop() # pop the (
            for item in temp:
                stack.append(item)
        else:
            stack.append(x)

    return "".join(stack)