matrix = [[1,2,3],[4,5,6],[7,8,9]]

def total(matrix):
    row = len(matrix)
    col = len(matrix[0])

    s1 = s2 = 0
    i=0; j=col-1;
    # while(i<row and j>=0):
    #     s1 += matrix[i][i]
    #     s2 += matrix[i][j]
    #     i += 1
    #     j -= 1
    
    while(i<row):
        s1 += matrix[i][i]
        s2 += matrix[i][col-1-i]
        i += 1

    if((row%2)!=0):
        return s1+s2-matrix[row//2][row//2]
    else:
        return s1+s2

print(total(matrix))
