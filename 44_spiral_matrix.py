# n = int(input("Enter number of rows u want : "))

# def spiral(n):
#     arr = [[0]*n for i in range(n)]
#     c = 1
#     for i in range(n):
#         arr[0][i] = c
#         c += 1
#     for i in range(1,n):
#         arr[i][n-1] = c
#         c += 1 
#     for i in range(n-2,-1,-1):
#         arr[n-1][i] = c
#         c += 1
#     for i in range(n-2,0,-1):
#         arr[i][0] = c
#         c += 1
#     for i in range(1,n-1):
#         arr[1][i] = c
#         c += 1
#     return arr    
# print(spiral(n))        

n = int(input("Enter number of rows u want"))

def spiral(n):
    arr = [[0]*n for i in range(n)]

    c = 1
    sr = 0
    sc = 0
    er = n
    ec = n
    while(c<=n*n):
        for i in range(sc,ec):
            arr[sr][i] = c
            c += 1
        sr += 1

        for i in range(sr,er):
            arr[i][ec-1] = c
            c += 1
        ec -= 1

        for i in range(ec-1,sc-1,-1):
            arr[er-1][i] = c
            c += 1
        er -= 1

        for i in range(er-1,sr-1,-1):
            arr[i][sc] = c
            c += 1
        sc += 1

    return arr

print(spiral(n))        