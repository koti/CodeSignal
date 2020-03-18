def allLongestStrings(inputArray):
    largest = len(max(inputArray, key=len))
    temp = []
    for j in range(len(inputArray)):
        if len(inputArray[j]) == largest:
            temp.append(inputArray[j])
    return temp
