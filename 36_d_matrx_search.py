
# def ele_matrx_serch(arr,target):
    
#     for i in range(len(arr)):

#         s = 0
#         e = len(arr[i]) - 1
#         while s < e:
#             mid = (s + e)//2
#             if target > arr[i][mid]:
#                 s = mid + 1
#             else:
#                 e = mid
#         if arr[i][s] == target:
#             print("The elem {} is present at {}".format(target,s))
#             return True
                    
#     return False

# arr = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# target = int(input("Enter a element::"))
# print(ele_matrx_serch(arr,target))   



# matrix = [
#     [1,4,7,11,15],
#     [2,5,8,12,19],
#     [3,6,9,16,22],
#     [10,13,14,17,24],
#     [18,21,23,26,30]
#     ]

# target = 18 

# def searchInMatrix(matrix, target):

#     rows = 0
#     n = len(matrix)
#     cols = len(matrix[0])-1

#     while rows < n and cols >= 0:
#         if matrix[rows][cols] == target:
#             return [rows, cols]

#         if matrix[rows][cols] < target:
#             rows += 1 
#         else:
#             cols -= 1 

#     return False 

# print(searchInMatrix(matrix, target))






# matrix = [
#     [1,4,7,11,15],
#     [2,5,8,12,19],
#     [3,6,9,16,22],
#     [10,13,14,17,24],
#     [18,21,23,26,30]
#     ]
matrix = [[1,3,5,7],
          [10,11,16,20],
          [23,30,34,60]]
target = 18    
def search_ele_in_matrX(matrix,target):
    l = 0 
    r =  (len(matrix[0]) * len(matrix))-1
    print("r", r)

    c = len(matrix[0])

    while l <= r:

        mid = (l + r)//2 

        i = mid//c 
        j = mid % c 

        if matrix[i][j] == target:
            return True

        elif target > matrix[i][j]:
            l = mid + 1 

        else:
            r = mid - 1

    return False  

print(search_ele_in_matrX(matrix,target))