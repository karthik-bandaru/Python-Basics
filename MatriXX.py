n = 3
# a = input() # 1 2 3  ===> a string with spaces inbetween
# b = input() # 4 5 6
# c = input() # 7 8 9

'''
1 2 3 
4 5 6
7 8 9 

output :   [
            [1,2,3]
            [7, 8 9]]
'''
matrix = []
for i in range(3):
    
    input_row = list(map(int, input().split(" ")))
    matrix.append(input_row)
    
print(matrix)