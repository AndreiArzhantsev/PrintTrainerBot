def Accuracy(pattern, result):
    len1 = len(pattern)
    len2 = len(result)
    final_pattern = "";
    final_result = "";
    penalty = [[[0, 0] for j in range(len2+1)] for i in range(len1+1)]
    for i in range (1, len1+1):
        penalty[i][0][0] = i 
        penalty[i][0][1] = 2  
    for j in range (1, len2+1):
        penalty[0][j][0] = j
        penalty[0][j][1] = 1
    for i in range(1, len1+1):
        for j in range(1, len2+1):
            same = (pattern[i-1] != result[j-1])
            penalty[i][j][0] = min(penalty[i][j-1][0]+1, min(penalty[i-1][j][0]+1, penalty[i-1][j-1][0]+same))
            if (min(penalty[i][j-1][0]+1, min(penalty[i-1][j][0]+1, penalty[i-1][j-1][0]+same)) == penalty[i][j-1][0]+1):
                penalty[i][j][1] = 1
            elif (min(penalty[i][j-1][0]+1, min(penalty[i-1][j][0]+1, penalty[i-1][j-1][0]+same)) == penalty[i-1][j][0]+1):
                penalty[i][j][1] = 2
            elif (min(penalty[i][j-1][0]+1, min(penalty[i-1][j][0]+1, penalty[i-1][j-1][0]+same)) == penalty[i-1][j-1][0]+same):
                penalty[i][j][1] = 3
    cur_i, cur_j = len1, len2

    while(penalty[cur_i][cur_j][1] != 0):
        if (penalty[cur_i][cur_j][1] == 1):
            final_pattern+="_"
            final_result+=result[cur_j-1]
            cur_j-=1
        elif (penalty[cur_i][cur_j][1] == 2):
            final_pattern+=pattern[cur_i-1]
            final_result+="_"
            cur_i-=1
        elif (penalty[cur_i][cur_j][1] == 3):
            if (result[cur_j-1] != pattern[cur_i-1]):
                final_pattern+=pattern[cur_i-1].upper()
                final_result+=result[cur_j-1].upper()
            else:
                final_pattern+=pattern[cur_i-1]
                final_result+=result[cur_j-1]
            cur_i-=1
            cur_j-=1
    final_result = final_result[::-1]
    final_pattern = final_pattern[::-1]
    length = 50
    chunk_result = [final_result[i:i+length] for i in range(0, len(final_result), length)]
    chunk_pattern = [final_pattern[i:i+length] for i in range(0, len(final_pattern), length)]
    final_typos = ""
    for i in range(len(chunk_result)):
        final_typos+=chunk_pattern[i]
        final_typos+="\n"
        final_typos+=chunk_result[i]
        final_typos+="\n\n"
    return [penalty[len1][len2][0], final_typos]
