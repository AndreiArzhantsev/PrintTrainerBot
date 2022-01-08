
def Accuracy(pattern, result):
    len1 = len(pattern)
    len2 = len(result)
    penalty = [[0 for j in range(len2+1)] for i in range(len1+1)]
    for i in range (len1+1):
        penalty[i][0] = i   
    for j in range (len2+1):
        penalty[0][j] = j
    for i in range(1, len1+1):
        for j in range(1, len2+1):
            same = (pattern[i-1] != result[j-1])
            penalty[i][j] = min(penalty[i][j-1]+1, min(penalty[i-1][j]+1, penalty[i-1][j-1]+same))
    return penalty[len1][len2]

