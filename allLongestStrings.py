def allLongestStrings(inputArray):
    '''max = max(inputArray, key=len)'''
    max = 0
    for i in range(len(inputArray)):
        if(len(inputArray[i])) > max:
            max = len(inputArray[i])
        else:
            pass

    temp = []
    for j in range(len(inputArray)):
        if len(inputArray[j]) == max:
            temp.append(inputArray[j])
    return temp
