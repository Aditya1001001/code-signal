"""Given an encoded string, return its corresponding decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square
brackets is repeated exactly k times. Note: k is guaranteed to be a positive integer.

Note that your solution should have linear complexity because this is what you will be asked during an interview.

Example:
For s = "4[ab]", the output should be
decodeString(s) = "abababab";

For s = "2[b3[a]]", the output should be
decodeString(s) = "baaabaaa";

For s = "z1[y]zzz2[abc]", the output should be
decodeString(s) = "zyzzzabcabc"."""


def decodeString(s):
    stack = []
    for x in s:
        if x == "]":
            temp = ""
            while stack[-1] != "[":
                temp += stack.pop()
            stack.pop() # pop the [
            # getting the number
            num = ""
            while stack[-1].isnumeric():
                num += stack.pop()
                if stack == []:
                    break
            num = int(num[::-1])
            stack = stack + num * list(temp[::-1])
        else:
            stack.append(x)

    return "".join(stack)
