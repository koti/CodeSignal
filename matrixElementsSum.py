import numpy as np


def matrixElementsSum(matrix):
    a = np.array(matrix)
    total = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            if (a[i][j] == 0) and (i < len(a) - 1):
                a[i + 1][j] = 0
            total += a[i][j]
    return total
