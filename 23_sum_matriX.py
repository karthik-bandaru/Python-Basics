mat1=[[1,2,3],[4,5,6],[7,8,9]]
mat2=[[11,12,13],[14,15,16],[17,18,19]]

mat1=[[1,2,3],[4,5,6],[7,8,9]]
mat2=[[11,12,13],[14,15,16],[17,18,19]]


def sum_of_two_matrices(mat1, mat2):
    
    mat1_rows = len(mat1)
    mat1_cols = len(mat1[0])
    
    mat2_rows = len(mat2)
    mat2_cols = len(mat2[0])
    
    if mat1_rows != mat2_rows and mat1_cols != mat2_cols:
        return "Not a square matrix. Hence addition is not possible"
    
    res = [[0]*mat1_cols for i in range(mat1_rows)]
    
    for i in range(mat1_rows):
        for j in range(mat1_cols):
            res[i][j] = (mat1[i][j] + mat2[i][j])
    
    return res 
    
print(sum_of_two_matrices(mat1, mat2))

