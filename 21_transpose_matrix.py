matrix = [[1,4,5], [6,7,2], [8,9,3]]



def transponse_matrix(matrix):
    
    row = len(matrix)
    col = len(matrix[0])
    transposed_matrix = [[0]*col for i in range(row)] 
    

    for i in range(row):
        for j in range(col):
            transposed_matrix[i][j] = matrix[j][i]
    
    return transposed_matrix 
    
print(transponse_matrix(matrix))


 