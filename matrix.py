rows=int(input("Enter number of Rows::"))
cols=int(input("Enter cols::"))
matrix=[]
for row in range(rows):
    row = []
    for col in range(cols):
        i=int(input("enter elem::"))
        row.append(i) 

    matrix.append(row)
print(matrix)
