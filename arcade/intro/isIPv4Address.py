def isIPv4Address(inputString):
    bits = inputString.split(".")
    if len(bits) == 4:
        for bit in bits:
            if bit.isnumeric():
                if int(bit) <= 255 and int(bit) >= 0:
                    pass
                else:
                    return False
            else:
                return False
        return True
    else:
        return False

print(isIPv4Address("172.16.254.1"))