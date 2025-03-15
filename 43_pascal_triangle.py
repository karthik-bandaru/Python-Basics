n = int(input("Enter rows::"))
print("line 2")
def pascal_triangle(n):
    print("line 4")
    arr = [[1]*(i+1) for i in range(n)]
    if n <= 2:
        return arr
    for i in range(2,n):
        for j in range(1,i):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
    return arr
print("line 11")
print("line 13",pascal_triangle(n))



    # [  [1],
    #   [1][1] ,
#      [1  1  1]    ,                             [ 1   2   1 ]           
#     [1  1  1  1],     i = 3, j = 1, j = i;     [ 1  3   3   1 ]
#   [1  1   1  1  1 ]   i = 4, j =1, j = i;     [ 1  4  6  4   1 ]
    # ]
 