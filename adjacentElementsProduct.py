def adjacentElementsProduct(inputArray):
    temp = []
    for i in range(len(inputArray) - 1):
        prod = inputArray[i] * inputArray[i + 1]
        temp.append(prod)
    return max(temp)
