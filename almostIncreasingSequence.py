def almostIncreasingSequence(sequence):
    s2 = sequence[:]
    deleted = 0
    if (len(sequence) - len(set(sequence))) > 1:
        return False
    elif len(set(sequence)) == 1:
        return True
    
    for i in range(len(sequence)-1):
        if s2[i] < s2[i+1]:
            continue
        else:
            del sequence[i:i+2]
            deleted += 1
            
    for i in range(len(sequence)-1):
        if sequence[i] > sequence[i+1]:
            return False
        
    if deleted > 1:
        return False
    else:
        return True
