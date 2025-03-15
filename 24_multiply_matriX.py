mat1=[[1,2,3],[4,5,6],[7,8,9]]
mat2=[[11,12,13],[14,15,16],[17,18,19]]


def multiplication_of_two_matrices(mat1, mat2):
    
    mat1_rows = len(mat1)
    mat1_cols = len(mat1[0])
    
    mat2_rows = len(mat2)
    mat2_cols = len(mat2[0])
    
    if mat1_cols != mat2_rows :
        return "matrix multiplication condition not satisfied"
    
    res = [[0]*mat2_cols for i in range(mat1_rows)]
    
    for i in range(len(res)):
        for j in range(len(res[0])):
            summ = 0 
            
            for k in range(mat1_cols):
                summ += mat1[i][k] + mat2[k][j]
            res[i][j] = summ    
            
    return res 
    
print(multiplication_of_two_matrices(mat1, mat2))




















