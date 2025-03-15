matrix=[[1,0,0],[0,1,0],[0,0,1]]

def singular_matrix(matrix):

    row=len(matrix)
    col=len(matrix[0])

    for i in range(row):
        for j in range(col):
            if matrix[i][i] == 1:
                continue
            if matrix[i][j] != 0:
                return False 

    return True        

print(singular_matrix(matrix))