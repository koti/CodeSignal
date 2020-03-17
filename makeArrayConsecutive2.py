def makeArrayConsecutive2(statues):
    statues.sort()
    additions = 0
    for i in range(len(statues) - 1):
        if (statues[i + 1] - statues[i]) > 1:
            additions = additions + (statues[i+1] - statues[i] - 1)
    return additions
