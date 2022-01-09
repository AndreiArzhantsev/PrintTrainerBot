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

def results(orig_text, your_text, time, book):
    accuracy_result = Accuracy(orig_text.strip(), your_text.strip())
    print("You made", accuracy_result, 2, "typos")
    print("Your accuracy is: ", round(100 - 100 * accuracy_result / len(orig_text), 2), "%", sep='')
    print("Time spent:", round(time, 2), "sec")
    print("Your speed: ", round(len(orig_text) / time, 2), "symbols/sec")
    print("This text was from:", book)
