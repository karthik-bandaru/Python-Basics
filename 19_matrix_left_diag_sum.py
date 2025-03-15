matrix = [[1,4,5], [6,7,2], [8,9,3]]


def matrix_left_diagonal_sum(matrix):
    result = 0 

    row = len(matrix)
    col = len(matrix[0])
    
    
    for i in range(row):
        result += matrix[i][col-i-1]

    return result 
    
print(matrix_left_diagonal_sum(matrix))

def matrix_right_diagonal_sum(matrix):
    row = len(matrix)
    col = len(matrix[0])
    result = 0
    for i in range(col):
        result += matrix[i][i]
    return result

print(matrix_right_diagonal_sum(matrix))   

def total_sum(matrix):
    row = len(matrix)
    col = len(matrix[0])
    s1 = s2 = 0
    i = 0; j = col - 1
    while (i<row and j >= 0):
        s1 += matrix[i][i]
        s2 += matrix[i][j]
        i += 1
        j -= 1
    if(row%2)!=0:
        return s1 + s2 - matrix[row//2][row//2]
    else:
        return s1+s2

print(total_sum(matrix))
    