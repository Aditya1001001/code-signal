"""Given a string, your task is to replace each of its characters by the next
one in the English alphabet; i.e. replace a with b, replace b with c, etc
(z would be replaced by a).

Example -
For inputString = "crazy", the output should be alphabeticShift(inputString) = "dsbaz". """

def alphabeticShift(inputString):
    return "".join(list(map(lambda c: chr(ord(c) + 1) if c!='z' else 'a',inputString)))
