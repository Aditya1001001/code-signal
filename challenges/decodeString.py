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


decodeString("4[ab]")