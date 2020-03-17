def checkPalindrome(inputString):
    rev = inputString[::-1]

    if rev == inputString:
        return True
    return False
