# n = [0,0,1,2,3,4,4,5,6,6,6,7,8,9,4,4]

# O = [0,1,2,3,4,5,6,7,8,9,4]


# print(len(n))
# for i in range(len(n)-3):
    
#     if(n[i] == n[i+1]):
#         del n[i+1]

# del n[2]
# print(len(n))

# res = []
# for i in range(len(n)-1):
#     if(n[i] != n[i+1] ):
#         res.append(n[i])
#         # i += 1
# res.append(n[len(n)-1])
# print(res)

# res = []
# i = 0
# while(i<len(n)-1):

#     ele = n[i]
#     # j = i                             # It is really wonderfulllll
#     res.append(ele)                         # if u write condition as 
#     while(i<len(n)-1 and ele == n[i+1]):    # ele == n[i+1] and i<len(n)-1
#         i += 1                              # then it rise an error
#     i += 1                                  # [n+1] index out of range...

# print(res)        


# res = []
# for i in range(len(n)-1):            # It does not workkk..
#     ele = n[i]                       # Must write in while loops only....
#     res.append(n[i])
#     while(i<len(n)-1 and ele == n[i+1]):
#         i += 1
# print(res)

n = [0,0,1,2,3,4,4,5,6,6,6,7,8,9,4]
res = []
i = 0
while(i < len(n)):
    ele = n[i]
    res.append(ele)

    while(i<len(n)-1 and ele == n[i+1]):
        i += 1

    i += 1
print(res)        




